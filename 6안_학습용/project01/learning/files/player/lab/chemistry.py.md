# `player/lab/chemistry.py`

측정된 호흡 대신 역할 보완 규칙으로 케미를 계산하는 순수 함수



[실제 코드 열기](../../../../player/lab/chemistry.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from math import sqrt

```

## 함수·클래스 안내

### `_num` — 99행

입력 이름: `v`

읽을 때 따라갈 호출(중복 제외): `float`



### `_per90` — 106행

입력 이름: `v`, `minutes`

읽을 때 따라갈 호출(중복 제외): `_num`



### `_rate` — 113행

입력 이름: `success`, `attempt`

읽을 때 따라갈 호출(중복 제외): `_num`



### `_percentile` — 120행

sorted_values 중 value 이하인 비율(0~100). 기준 집단이 비면 50.

입력 이름: `value`, `sorted_values`

읽을 때 따라갈 호출(중복 제외): `len`



### `raw_metrics` — 140행

s: 선수 기록(dict). 90분당/성공률 지표로 변환.

입력 이름: `s`

찾아볼 반환 사전 키(분기·내부 함수 포함): `goals`, `assists`, `shots`, `shots_on_target`, `key_passes`, `dribble`, `cross`, `pass_rate`, `pass_volume`, `recoveries`, `interceptions`, `tackle`, `clearances`, `blocks`, `aerial_duel`, `ground_duel`, `dribble_attempt`, `shot_accuracy`, `goal_conversion`, `card_rate`, `rating`, `best11_rate`, `mom_rate`

읽을 때 따라갈 호출(중복 제외): `s.get`, `_per90`, `_rate`, `_num`



### `_assign_styles` — 172행

플레이 스타일 부여. 출전이 충분한 선수에게만, 최대 S.MAX_STYLES 개.

입력 이름: `pos`, `met`, `ref_pos`

읽을 때 따라갈 호출(중복 제외): `S.STYLES.items`, `found.sort`, `found.append`, `_percentile`, `sum`, `len`, `st.get`, `ref_pos.get`, `round`



### `build_profiles` — 193행

rows: [{'player_id','name','position','team_id','minutes', ...기록 필드...}]
반환: {player_id: profile}
  profile = {id,name,position,team_id,minutes,low_minutes, cats:{카테고리:0~100}, traits:[카테고리...]}
백분위의 기준 집단은 같은 포지션 + 출전 REFERENCE_MIN_MINUTES 이상 선수들이다.
기준 집단에 없는 선수(출전 적음)도 같은 기준표로 점수를 매긴다.

입력 이름: `rows`

읽을 때 따라갈 호출(중복 제외): `(r.get('position') or '').strip().upper`, `prepared.append`, `met.items`, `CATEGORIES[pos].items`, `_num`, `ref.setdefault(pos, {}).setdefault(k, []).append`, `ref[pos][k].sort`, `r.get`, `_assign_styles`, `(r.get('position') or '').strip`, `raw_metrics`, `_percentile`, `sum`, `len`, `ref.get`, `ref.setdefault(pos, {}).setdefault`, `ref.get(pos, {}).get`, `cats.items`, `ref.setdefault`



### `_ability` — 252행

선수의 항목 백분위 평균 (케미 계산용 단순 능력 지표).

입력 이름: `p`

읽을 때 따라갈 호출(중복 제외): `list`, `p['cats'].values`, `sum`, `len`



### `_complement` — 258행

역할 보완 점수(0~100, 중립 50) 와 근거.
두 선수가 공통으로 가진 항목마다
  한쪽이 약점(<=WEAK_PCT)인데 다른 쪽이 강점(>=STRONG_PCT)이면 +1 (보완)
  둘 다 약점이면 -1 (약점 중복)

입력 이름: `a`, `b`

읽을 때 따라갈 호출(중복 제외): `min`, `covered.append`, `len`, `overlap.append`, `_ability`



### `_geo` — 287행

입력 이름: `x`, `y`

읽을 때 따라갈 호출(중복 제외): `sqrt`, `max`



### `_link` — 291행

인접 라인 연계 점수(0~100) 와 근거 문구. 인접하지 않으면 (None, '').
FW<->MF : 미드필더의 찬스 창출 x 공격수의 득점력
MF<->DF : 수비수의 수비 가담 x 미드필더의 빌드업
DF<->GK : 수비수의 수비 가담 (골키퍼는 이 지표 하나만 반영)

입력 이름: `a`, `b`

읽을 때 따라갈 호출(중복 제외): `df['cats'].get`, `_geo`, `mf['cats'].get`, `fw['cats'].get`



### `pair_chemistry` — 322행

두 선수 프로필의 케미. 순서를 바꿔도 같은 값(대칭).

입력 이름: `a`, `b`

찾아볼 반환 사전 키(분기·내부 함수 포함): `a`, `b`, `score`, `tier`, `bonus`, `overlap`, `style_adj`, `reasons`

읽을 때 따라갈 호출(중복 제외): `_complement`, `_link`, `a.get`, `max`, `reasons.extend`, `b.get`, `min`, `reasons.append`, `round`, `S.COMPAT.get`, `bool`, `frozenset`, `style_reasons.append`, `', '.join`



### `_counts_for_lineup` — 406행

라인업 안에서 케미를 계산할 쌍인가: 같은 라인 + 인접한 라인.

입력 이름: `a`, `b`



### `lineup_chemistry` — 416행

lineup: 프로필 리스트(11명). scale: '케미 중시' 슬라이더(0=끔, 1=기본, 2=두 배).
반환:
  players: {player_id: {'bonus':가산점, 'pairs':[케미 있는 상대...]}}
  team_score: 11명 가산점 평균
  pairs: 계산한 모든 쌍

입력 이름: `lineup`, `scale`

찾아볼 반환 사전 키(분기·내부 함수 포함): `players`, `team_score`, `pairs`

읽을 때 따라갈 호출(중복 제외): `range`, `len`, `round`, `pair_chemistry`, `pairs.append`, `max`, `sorted`, `sum`, `_counts_for_lineup`, `min`, `per_player[me['id']]['partners'].append`, `players.values`



### `final_score` — 468행

최종 점수 = 능력 + 케미 가산 + 이후 추가될 가산(extra). FINAL_SCORE_CAP 을 넘지 않는다.

입력 이름: `ability`, `chemistry_bonus`, `extra`

읽을 때 따라갈 호출(중복 제외): `min`



### `recommend_partners` — 478행

player 와 케미가 좋은 선수를 pool(프로필 리스트)에서 찾는다.
같은 라인이거나 인접한 라인이고, 케미 점수가 min_score 이상인 선수만 추천한다.
반환: 케미 점수 높은 순 리스트

입력 이름: `player`, `pool`, `k`, `min_score`

읽을 때 따라갈 호출(중복 제외): `out.sort`, `pair_chemistry`, `out.append`, `_counts_for_lineup`



### `load_profiles` — 538행

PlayerStats(해당 시즌)에서 프로필을 만든다. 관리자 제외선수는 exclude_ids 로 뺀다.

입력 이름: `season`, `exclude_ids`

읽을 때 따라갈 호출(중복 제외): `PlayerStats.objects.filter(season=season, minutes__gt=0).exclude(player_id__in=list(exclude_ids)).select_related`, `build_profiles`, `row.update`, `rows.append`, `PlayerStats.objects.filter(season=season, minutes__gt=0).exclude`, `getattr`, `PlayerStats.objects.filter`, `list`

