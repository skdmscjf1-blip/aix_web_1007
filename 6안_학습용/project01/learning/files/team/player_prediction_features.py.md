# `team/player_prediction_features.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../team/player_prediction_features.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import math

from player.gk_evaluation import TEAM_NAMES

from player.services import get_filtered_best11

from team.models import Team

```

## 함수·클래스 안내

### `find_team` — 27행

예측 화면의 구단명을 선수 DB의 구단과 연결합니다.

입력 이름: `name`

읽을 때 따라갈 호출(중복 제외): `len`, `ValueError`, `Team.objects.all`, `TEAM_NAMES.get`



### `team_scores` — 41행

BEST11의 포지션별 평균점수를 계산합니다.

입력 이름: `team`

읽을 때 따라갈 호출(중복 제외): `get_filtered_best11`, `set`, `EXPECTED_COUNTS.items`, `str`, `len`, `ValueError`, `float`, `selected.add`, `values.append`, `sum`, `math.isfinite`



### `build_player_features` — 82행

양 팀 선수 점수와 예측 입력용 차이를 만듭니다.

입력 이름: `home_name`, `away_name`

찾아볼 반환 사전 키(분기·내부 함수 포함): `available`, `formation`, `home_name`, `away_name`, `values`, `rows`, `message`

읽을 때 따라갈 호출(중복 제외): `find_team`, `team_scores`, `round`, `rows.append`, `ValueError`, `str`

