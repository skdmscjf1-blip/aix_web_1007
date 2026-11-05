"""수정 전후 결과를 JSON으로 남깁니다. 원본 DB에는 읽기만 허용합니다."""
import json,sys,hashlib
from pathlib import Path
import os
PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))
os.environ['DJANGO_SETTINGS_MODULE'] = 'learning.readonly_settings'
import django
django.setup()
from player import services as S,scoring as SC
from player.lab.service import Ctx
from player.models import PlayerStats
from team.models import Team
from simulation.models import SimulationRun
from simulation.tracking_metrics import extract_player_tracking
from team.match_prediction import poisson_probabilities
from team.lineup_simulation import SimulationContext,player_probabilities,team_strength

def clean(v):
 if isinstance(v,dict):return {str(k):clean(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [clean(x) for x in v]
 if hasattr(v,'_meta'):return {'model':v._meta.label,'pk':str(v.pk)}
 return v
out={'official':clean(S.get_best11()),'formations':{},'radar':{},'tracking':{},'weights':{}}
for pos in SC.POSITIONS:out['weights'][pos]=SC.metric_weights(pos)
for team in [None]+list(Team.objects.values_list('pk',flat=True))+['bad','0','9999']:
 for form in list(S.FORMATIONS)+['bad']:
  result=S.get_filtered_best11(team,form)
  if team and str(team).isdigit() and int(team)>0:
   assert all(row['player'].team_id==int(team) for rows in result['best11'].values() for row in rows)
  out['formations'][f'{team}:{form}']=clean(result)
for stats in PlayerStats.objects.select_related('player').order_by('player_id'):
 out['radar'][stats.player_id]=clean(S.get_player_radar(stats.player_id))
for options in [{},{'preset':'default','mult':{'goals':1.5},'chem_scale':.5,'exp_scale':1.0}]:
 ctx=Ctx(options);out.setdefault('lab',[]).append(clean(ctx.ability))
for run in SimulationRun.objects.filter(generator_version='possession-engine-v2').order_by('pk'):
 out['tracking'][str(run.pk)]=extract_player_tracking(run.document)
out['poisson']=[poisson_probabilities(a,b) for a,b in [(1.5,1),(0.2,4),(2,2)]]
ctx=SimulationContext();out['reference']=ctx.lineup_reference()
# 실제 명단과 조건을 사용하는 선수 확률도 비교합니다.
ids=list(ctx.db_teams)[:2]
out['recommended']={str(t):clean(ctx.recommended(t,'4-3-3')) for t in ids}
encoded = json.dumps(clean(out), ensure_ascii=False, sort_keys=True, allow_nan=False)
actual = hashlib.sha256(encoded.encode('utf-8')).hexdigest()
expected = json.loads((PROJECT / 'learning' / 'verification_baseline.json').read_text(encoding='utf-8'))
if actual != expected['result_sha256']:
    raise SystemExit('기준 결과와 다릅니다. 데이터·설정·실행 환경 또는 계산 변경을 확인하세요.')
print('통과: 정리 전 기준 결과와 일치합니다.')
print('포메이션 조합',len(out['formations']),'레이더',len(out['radar']),'GPS 경기',len(out['tracking']))
