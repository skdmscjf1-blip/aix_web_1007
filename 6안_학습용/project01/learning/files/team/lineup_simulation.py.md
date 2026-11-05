# `team/lineup_simulation.py`

명단 검증·선수 점수·공격/수비 지수·팀/선수 확률 혼합



[실제 코드 열기](../../../team/lineup_simulation.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from collections import Counter

from datetime import date

import math

from player.gk_evaluation import TEAM_NAMES, load_snapshot, match_record, official_metrics

from player.models import Player, PlayerStats

from player.services import FORMATIONS, FW_WEIGHTS, MF_WEIGHTS, DF_WEIGHTS, GK_WEIGHTS, get_formation_candidates, calculate_position_scores, get_fw_metrics, get_mf_metrics, get_df_metrics, get_filtered_best11, number, per90

from team.models import Team

from team.match_prediction import PredictionUnavailable, load_matches, load_bundle, team_options, forecast, features_for, predict_probabilities, poisson_probabilities

from team import virtual_stats

```

## 함수·클래스 안내

### `player_score_context` — 80행

BEST11 연구실과 같은 선수 점수 계산 도구를 준비합니다.

입력 이름: `settings`

읽을 때 따라갈 호출(중복 제외): `LAB.Ctx`, `options.get`



### `slots` — 95행

포메이션을 GK→DF→MF→FW 자리 목록으로 펼칩니다.

입력 이름: `formation`

읽을 때 따라갈 호출(중복 제외): `PredictionUnavailable`, `range`, `positions.append`



### `SimulationContext` — 106행

클래스 안의 작업: `__init__`, `lineup_reference`, `chem_scores`, `bonus_reference`, `ability`, `roster`, `recommended`, `validate_lineup`



### `player_weight` — 426행

승부예측에서 '선수 능력치' 부분의 비중. 관리자 > 점수 기준의 값(없으면 30%).

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `config.player_weight`



### `_mean` — 436행

입력 이름: `values`, `default`

읽을 때 따라갈 호출(중복 제외): `list`, `sum`, `len`



### `team_strength` — 441행

라인업의 공격·수비 지수. 공격 = 공격수·미드필더 평균, 수비 = 수비수 60% + 골키퍼 40%.
scores 를 주면(내 BEST11 가중치) 그 점수로, 아니면 통합 점수(effective_score)로 계산한다.

입력 이름: `lineup`, `scores`

찾아볼 반환 사전 키(분기·내부 함수 포함): `attack`, `defense`

읽을 때 따라갈 호출(중복 제외): `_mean`, `scores.get`, `min`, `round`, `score`



### `player_probabilities` — 459행

선수 능력치만으로 본 확률 (팀 기록과 독립).
리그 평균 홈·원정 득점(base)에서 출발해, 공격 지수 ÷ 상대 수비 지수 (기본 선발 라인업 평균 대비)로
예상 득점을 조정한 뒤 포아송으로 승·무·패를 낸다.

입력 이름: `base_home`, `base_away`, `home`, `away`, `reference`, `home_form`

읽을 때 따라갈 호출(중복 제외): `factor`, `max`, `min`, `poisson_probabilities`, `round`



### `best11_recent` — 483행

내 BEST11의 '가상' 최근 5경기. 같은 11명이면 항상 같은 결과가 나온다(선수 ID가 씨앗).
라인업 능력이 높을수록 이길 확률이 조금 높게 만든다. 실제 경기 결과가 아니다.

입력 이름: `lineup`, `home_name`, `opponents`

찾아볼 반환 사전 키(분기·내부 함수 포함): `team`, `games`, `points_per_game`, `form_factor`, `note`

읽을 때 따라갈 호출(중복 제외): `sorted`, `random.Random`, `_mean`, `max`, `range`, `min`, `rng.random`, `rng.choice`, `games.append`, `sum`, `round`, `','.join`, `map`, `rng.randint`



### `department_scores` — 528행

입력 이름: `lineup`

읽을 때 따라갈 호출(중복 제외): `sum`



### `adjust_probabilities` — 540행

입력 이름: `prior`, `home_change`, `away_change`

읽을 때 따라갈 호출(중복 제외): `max`, `sum`, `min`, `weighted.values`, `math.exp`, `weighted.items`, `abs`



### `percent_rows` — 573행

입력 이름: `probabilities`

읽을 때 따라갈 호출(중복 제외): `sorted`, `int`, `sum`, `values.values`



### `bounded_display` — 592행

반올림 후에도 결과별 최대 8%포인트 변화를 지킵니다.

입력 이름: `prior`, `adjusted`

읽을 때 따라갈 호출(중복 제외): `percent_rows`, `round`, `max`, `min`, `sum`, `percent_rows(adjusted).items`, `units.items`, `units.values`



### `simulate` — 643행

입력 이름: `context`, `payload`

찾아볼 반환 사전 키(분기·내부 함수 포함): `home_name`, `away_name`, `date`, `long_gap`, `stale_days`, `probabilities`, `home`, `away`, `player_part`, `best11_recent`, `best11_weighted`, `bonus_result`, `views`, `baseline_accuracy`, `test_count`

읽을 때 따라갈 호출(중복 제외): `payload.get`, `forecast`, `features_for`, `predict_probabilities`, `player_weight`, `context.lineup_reference`, `player_probabilities`, `context.bonus_reference`, `context.chem_scores`, `isinstance`, `PredictionUnavailable`, `date.fromisoformat`, `context.validate_lineup`, `department_scores`, `sum`, `teams.append`, `team_strength`, `best11_recent`, `percent_rows`, `player_score_context`, `t.pop`, `round`, `context.recommended`, `normal_by_id.get`, `bonus_rows`, `changes.append`, `bonus.get`, `bonus_player.items`

