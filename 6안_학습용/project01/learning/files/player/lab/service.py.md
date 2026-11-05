# `player/lab/service.py`

연구실 데이터·사용자 비중·경험 보정·케미·보고서를 연결하는 서버 계산



[실제 코드 열기](../../../../player/lab/service.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import glob

import os

import time

from datetime import date, timedelta

from django.conf import settings

from player.models import PlayerStats

from player import services as SV

from . import chemistry as CH

from . import management as MG

from . import analysis as AN

from . import club_profile as CP

from . import tuning as TU

from . import quality as QL

from player import scoring as SC

```

## 함수·클래스 안내

### `base_weights` — 60행

관리자 기본 범주 비중으로 포지션별 컬럼 가중치를 만듭니다.

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `SV.position_weights`



### `_expand_old` — 68행

예전 지표 이름(goals, clearances …)으로 된 배율을 새 컬럼 이름으로 바꾼다 (프리셋·상대 맞춤용).

입력 이름: `mult`

읽을 때 따라갈 호출(중복 제외): `(mult or {}).items`, `SC.OLD_KEYS.get`, `out.get`



### `_load` — 135행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `time.time`, `PlayerStats.objects.filter(season=SEASON, minutes__gt=0).exclude(player_id__in=SV.EXCLUDED_PLAYER_IDS).select_related`, `CP.classify`, `CH.build_profiles`, `stats_by_id.items`, `_cache.update`, `(st.player.position or '').strip().upper`, `row.update`, `rows.append`, `CP.team_metrics`, `club.get`, `PlayerStats.objects.filter(season=SEASON, minutes__gt=0).exclude`, `getattr`, `(pl.position or '').strip().upper`, `(st.player.position or '').strip`, `dict`, `AN.short_name`, `PlayerStats.objects.filter`, `stats_by_id.values`, `(pl.position or '').strip`



### `clear_cache` — 208행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `_cache.update`



### `build_weights` — 216행

기본 비중에 프리셋·사용자 설정·상대 맞춤 배율을 적용합니다.

mult: 사용자가 바꾼 배율. 'FW:goals90'처럼 포지션을 지정할 수 있습니다.
extra: 상대 맞춤 배율. 마지막에 추가로 곱합니다.
반환: {포지션: {컬럼 키: 비중}}이며 포지션마다 합계는 100입니다.

입력 이름: `preset`, `mult`, `extra`

읽을 때 따라갈 호출(중복 제외): `PRESETS.get`, `_expand_old`, `(mult or {}).items`, `base_weights().items`, `SC.group_of`, `base.items`, `raw_weights.items`, `max`, `str`, `base_weights`, `preset_multipliers.get`, `position_multipliers.get`, `sum`, `min`, `extra.get`, `raw_weights.values`, `float`



### `_shrunk` — 262행

짧게 뛴 선수의 기록을 평균 가까이 옮기는 기존 규칙입니다.

입력 이름: `vals`, `norm`, `f`

읽을 때 따라갈 호출(중복 제외): `vals.items`, `norm.mean.get`



### `ability_scores` — 279행

입력 이름: `weights`, `shrink`, `exp_scale`

읽을 때 따라갈 호출(중복 제외): `_load`, `data['stats'].items`, `by_position.items`, `stats.player.position.strip().upper`, `by_position.setdefault(position, []).append`, `SC.Normalizer`, `metric_function`, `position_weights.keys`, `metrics[player_id].items`, `sum`, `round`, `stats.player.position.strip`, `by_position.setdefault`, `reference_ids.append`, `normalizer.fill`, `_shrunk`, `contributions.append`, `max`, `min`, `normalizer.unit`



### `schedule` — 339행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `os.path.join`, `sorted`, `str`, `glob.glob`, `os.path.getmtime`, `_sched.update`, `MG.load_schedule`



### `_forecast_tools` — 352행

팀원이 만든 team.match_prediction 을 그대로 사용한다. 못 불러오면 (None, 이유).

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `MP.load_matches`, `MP.load_bundle`, `str`, `MP.team_options`



### `_meta` — 367행

입력 이름: `info`, `today`

읽을 때 따라갈 호출(중복 제외): `str`, `MG.age_on`, `info.items`



### `_parse_date` — 381행

입력 이름: `v`, `default`

읽을 때 따라갈 호출(중복 제외): `date.fromisoformat`, `str`



### `clean_log` — 388행

브라우저가 보낸 모의 경기 기록을 정리한다. 형식: [{'date':'YYYY-MM-DD','ids':[선수ID...]}] (최대 60건)

입력 이름: `raw`

읽을 때 따라갈 호출(중복 제외): `out.sort`, `_parse_date`, `isinstance`, `e.get`, `out.append`, `ids.append`, `int`



### `replay_mock` — 407행

모의 경기 기록(log)을 날짜순으로 다시 계산해서 target_date 킥오프 직전의 상태를 돌려준다.
- 경기에 나온 선수는 90분 출전(피로 누적, 연속 출전 횟수 +1).
- 같은 경기에 나온 구단의 나머지 선수는 '쉬었음'으로 보고 연속 출전이 끊긴다.
- 그 경기와 상관없는 구단 선수는 아무것도 바뀌지 않고, 시간이 지난 만큼만 회복한다.
- target_date 이후(같은 날 포함)의 기록은 반영하지 않는다.

입력 이름: `info`, `meta`, `log`, `target_date`

읽을 때 따라갈 호출(중복 제외): `MG.initial_state`, `state.items`, `MG.advance_round`, `state.update`, `max`, `dict`, `info.items`, `str`, `MG.pre_match_fatigue`, `last.get`, `timedelta`



### `goal_table` — 450행

{구단 DB id: {'gf': 경기당 득점, 'ga': 경기당 실점}} — 팀원의 경기 결과 파일에서. 못 읽으면 빈 dict.

입력 이름: `info`

읽을 때 따라갈 호출(중복 제외): `_forecast_tools`, `info.values`, `m.get`, `short_to_id.get`, `acc.items`, `acc.setdefault`



### `Ctx` — 482행

클래스 안의 작업: `__init__`, `pool`, `adj`, `lineup_profiles`, `score_lineup`, `badges`, `brief`



### `api_init` — 604행

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `teams`, `club_styles`, `formations`, `presets`, `metrics`, `today`, `prediction`, `schedule_note`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `sorted`, `_forecast_tools`, `c.today.isoformat`, `c.info.values`, `PRESETS.items`, `round`, `SC.group_weights(pos).get`, `SC.label`, `SC.group_weights`



### `_default_lineup` — 653행

입력 이름: `c`

읽을 때 따라갈 호출(중복 제외): `c.pool`, `cands.sort`, `c.adj`



### `api_lineup` — 666행

기본 라인업(능력 순) 또는 케미까지 반영해 다듬은 라인업(optimize=true).

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `lineup`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `_default_lineup`, `body.get`, `c.lineup_profiles`, `c.pool`, `range`, `len`, `c.score_lineup`, `cands.sort`, `list`, `c.adj`



### `_validate_lineup` — 700행

입력 이름: `c`, `body`

읽을 때 따라갈 호출(중복 제외): `body.get`, `int`, `ids.append`



### `api_evaluate` — 712행

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `error`, `players`, `total`, `chem_team`, `partial`, `opponent`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `_validate_lineup`, `c.lineup_profiles`, `c.score_lineup`, `set`, `recs.sort`, `c.pool`, `AN.irreplaceability`, `AN.lineup_report`, `bool`, `c.brief`, `d.update`, `round`, `_chem_reason`, `players.append`, `next`, `CH.recommend_partners`, `c.adj`, `c.ability.get`, `body.get`, `len`, `c.badges`, `CH.final_score`, `recs.append`, `c.profiles.values`, `c.info.values`



### `_outlook` — 824행

입력 이름: `c`, `lineup`

찾아볼 반환 사전 키(분기·내부 함수 포함): `available`, `rows`, `factor`, `trained_through`, `note`, `reason`

읽을 때 따라갈 호출(중복 제외): `_forecast_tools`, `next`, `AN.lineup_strength_factor`, `AN.opponent_outlook`, `MP.forecast`, `sum`, `max`, `len`, `round`, `c.profiles.values`, `c.info.values`, `c.adj`



### `_rotation` — 869행

남은 정규 라운드 로테이션 계획. 지금까지 모의 경기로 쌓인 피로(target 날짜 기준)에서 출발한다.

입력 이름: `c`, `lineup`

읽을 때 따라갈 호출(중복 제외): `next`, `AN.plan_rotation`, `c.ability.get`, `c.profiles.values`, `sorted`, `c.info.values`



### `api_condition` — 891행

모의 경기 화면용: 이 날짜에 이 선수들의 피로 상태. 피로가 많으면 '안 좋음' 컨디션을 제안한다.
body: {mock_log:[{date,ids}], date:'YYYY-MM-DD', ids:[선수ID...]}

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `players`, `date`, `records`, `bad_from`

읽을 때 따라갈 호출(중복 제외): `_parse_date`, `_meta`, `replay_mock`, `_load`, `body.get`, `date.today`, `clean_log`, `MG.card_probability`, `MG.fatigue_tier`, `target.isoformat`, `len`, `int`, `str`, `round`, `MG.availability`



### `api_schedule` — 928행

모의 경기 화면용: 한 팀 선발 11명 기준으로 남은 정규 일정 예상(다음 상대)과 로테이션 계획.
body: {mock_log:[{date,ids}], date:'YYYY-MM-DD', ids:[선수ID 11명]}
피로는 모의 경기 기록을 기준으로 하고, 팀은 선수들의 소속으로 정한다.

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `team`, `mixed`, `outlook`, `rotation`, `date`, `error`

읽을 때 따라갈 호출(중복 제외): `dict`, `_load`, `max`, `Ctx`, `c.lineup_profiles`, `len`, `set`, `_outlook`, `_rotation`, `c.target.isoformat`, `body.get`, `int`, `ids.append`, `teams.count`



### `api_candidates` — 964행

교체 후보: out_id 자리에 넣었을 때 라인업 총점이 높은 순. 맨 위가 '추천'이다.

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `candidates`, `position`, `error`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `_validate_lineup`, `c.lineup_profiles`, `ids.index`, `c.score_lineup`, `set`, `cands.sort`, `rows.sort`, `enumerate`, `_empty_slot_candidates`, `int`, `list`, `c.brief`, `d.update`, `rows.append`, `body.get`, `c.pool`, `c.badges`, `round`, `c.adj`, `CH.final_score`



### `_empty_slot_candidates` — 1013행

빈 칸 후보: 지금까지 고른 선수(0~10명)에 더했을 때 라인업 총점이 많이 오르는 순. 맨 위가 '추천'이다.

입력 이름: `c`, `ids`, `pos`

찾아볼 반환 사전 키(분기·내부 함수 포함): `candidates`, `position`

읽을 때 따라갈 호출(중복 제외): `c.lineup_profiles`, `set`, `cands.sort`, `rows.sort`, `enumerate`, `c.score_lineup`, `c.brief`, `d.update`, `rows.append`, `c.pool`, `c.badges`, `round`, `c.adj`, `CH.final_score`



### `api_formations` — 1043행

포메이션별 점수. 같은 설정(가중치·케미·구단)에서 6개 포메이션의 자동 선발 라인업을 만들어 점수로 비교한다.
- 점수 = 선수별 최종 점수(능력 + 케미, 상한 200점)의 합.
- 포메이션마다 포지션 인원이 달라 합계만 보면 인원이 많은 쪽이 유리하므로,
  '리그 같은 포지션 주전급(450분 이상) 평균 대비 +몇 점'(vs_avg)을 순위 기준으로 쓴다. 백분위는 쓰지 않는다.

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `formations`, `best`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `rows.sort`, `enumerate`, `_default_lineup`, `c.lineup_profiles`, `c.score_lineup`, `sum`, `rows.append`, `len`, `by_pos.setdefault`, `c.profiles.values`, `CH.final_score`, `round`, `by_pos.items`, `c.adj`



### `_short_reason` — 1096행

케미 이유를 짧게: '보완: 찬스 창출' -> '찬스 창출 보완', '연계: 찬스 창출→득점력' -> '연계', '같은 구단' 은 마지막에.

입력 이름: `reasons`

읽을 때 따라갈 호출(중복 제외): `'·'.join`, `r.startswith`, `out.append`, `seen.append`



### `_chem_reason` — 1115행

카드 옆에 작게 적는 케미 이유 한 줄. 가장 잘 맞는 상대, 가산이 없거나 감점이면 그 이유.

입력 이름: `me`, `lineup`, `cp`

읽을 때 따라갈 호출(중복 제외): `_short_reason`, `CH.pair_chemistry`, `CH._counts_for_lineup`, `J`



### `api_chem_partners` — 1133행

선수 한 명의 케미 파트너. 현재 라인업 안의 상대별 케미 점수·등급·이유, 그리고 라인업 밖(리그 전체)에서 케미가 좋은 후보.

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `player`, `chem_bonus`, `inside`, `outside`, `rule`, `error`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `_validate_lineup`, `c.profiles.get`, `c.lineup_profiles`, `inside.sort`, `set`, `CH.recommend_partners`, `int`, `CH.pair_chemistry`, `inside.append`, `dict`, `outside.append`, `c.score_lineup`, `body.get`, `len`, `me.get`, `CH._counts_for_lineup`, `c.profiles.values`



### `_jong` — 1192행

마지막 글자의 받침 번호(없으면 0, 한글이 아니면 0).

입력 이름: `word`

읽을 때 따라갈 호출(중복 제외): `(word or '').rstrip`, `ord`



### `J` — 1199행

조사 붙이기: 을/를, 이/가, 와/과, 으로/로 (이름이 받침으로 끝나는지에 따라).

입력 이름: `word`, `kind`

읽을 때 따라갈 호출(중복 제외): `_jong`



### `_evidence` — 1231행

지표 한 줄 근거: 기록 · 주전급 평균 대비 · 순위.

입력 이름: `r`



### `_breakdown` — 1244행

선수 한 명의 능력 점수를 지표별로 쪼갠다. ability_scores 와 같은 식이라 합계가 능력 점수와 일치한다(보정 전 합계 × 경험 배율).

입력 이름: `c`, `pid`

찾아볼 반환 사전 키(분기·내부 함수 포함): `rows`, `shrink`, `experience`, `ref_count`

읽을 때 따라갈 호출(중복 제외): `st.player.position.strip().upper`, `SC.Normalizer`, `rows.sort`, `fn`, `w.keys`, `norm.fill`, `_shrunk`, `sum`, `round`, `rows.append`, `max`, `len`, `st.player.position.strip`, `data['stats'].items`, `mets[pid].items`, `raw.get`, `norm.unit`, `getattr`, `norm.mean.get`, `s2.player.position.strip().upper`, `METRIC_LABELS.get`, `better`, `norm.hi.get`, `s2.player.position.strip`



### `api_player_report` — 1318행

BEST11 선수 팝업용 분석 보고서. 모든 문장에 근거 숫자(기록·주전급 평균·순위·점수 차이)를 붙인다.
- 왜 이 점수인가: 지표별 기여 + 보정(소표본·경험) + 케미
- 왜 쓰는가: 강점의 근거, 이 자리에서 대체 1순위와의 차이, 빠졌을 때 총점 변화
- 주의점·대안: 약점·표본·경고 위험, 더 나은 대안

입력 이름: `body`

찾아볼 반환 사전 키(분기·내부 함수 포함): `player`, `verdict`, `conclusion`, `rule`, `basis`, `confidence`, `h2h`, `ability`, `chem_bonus`, `final`, `rank`, `rank_total`, `top_pct`, `rows`, `why`, `hire`, `cautions`, `alternatives`, `irreplaceability`, `notes`, `error`

읽을 때 따라갈 호출(중복 제외): `Ctx`, `_validate_lineup`, `c.lineup_profiles`, `c.score_lineup`, `c.ability.get`, `CH.final_score`, `_breakdown`, `sorted`, `max`, `AN.irreplaceability`, `next`, `api_candidates`, `c.badges`, `why.append`, `bg.get`, `int`, `c.adj`, `_evidence(r).replace`, `sum`, `round`, `c.pool`, `dict`, `getattr`, `hire.append`, `cautions.append`, `len`, `body.get`, `str`



### `api_quality` — 1576행

선수 기록 데이터 점검 리포트. 관리자 제외선수·테스트 선수를 포함한 DB 전체(2026 시즌, 출전 기록 있는 선수)를 본다.

입력 이름: `body`

읽을 때 따라갈 호출(중복 제외): `PlayerStats.objects.filter(season=SEASON).select_related`, `QL.check`, `d.update`, `rows.append`, `PlayerStats.objects.filter`, `getattr`, `set`

