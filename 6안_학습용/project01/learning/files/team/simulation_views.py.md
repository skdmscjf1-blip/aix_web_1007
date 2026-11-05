# `team/simulation_views.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../team/simulation_views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from datetime import date, timedelta

import json

from django.http import JsonResponse

from django.shortcuts import render

from django.utils import timezone

from django.views.decorators.http import require_GET, require_POST

from player.services import FORMATIONS

from team.lineup_simulation import SimulationContext, simulate

from team.match_prediction import PredictionUnavailable

from team.player_comparison import attach_comparisons

```

## 함수·클래스 안내

### `_best11_request` — 17행

BEST11 화면에서 넘어온 내 라인업. 형식이 틀리면 None (화면은 평소처럼 연다).

입력 이름: `request`, `simulation`

찾아볼 반환 사전 키(분기·내부 함수 포함): `team`, `formation`, `players`

읽을 때 따라갈 호출(중복 제외): `request.GET.get`, `next`, `_best11_settings`, `team_pk.isdigit`, `int`, `len`, `raw.split`, `set`, `simulation.db_teams.items`



### `_best11_settings` — 44행

BEST11 화면의 내 가중치 설정(프리셋·지표별 가중치·케미·경험). 형식이 틀리면 기본값.

입력 이름: `raw`

찾아볼 반환 사전 키(분기·내부 함수 포함): `settings`, `settings_summary`

읽을 때 따라갈 호출(중복 제외): `isinstance`, `s.get`, `num`, `parts.append`, `' · '.join`, `json.loads`, `list`, `max`, `s['mult'].items`, `min`, `float`, `len`, `str`



### `simulation_page` — 86행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `render`, `SimulationContext`, `date.fromisoformat`, `_best11_request`, `simulation.db_teams.get`, `teams.append`, `list`, `max(timezone.localdate(), last_day + timedelta(days=1)).isoformat`, `(last_day + timedelta(days=1)).isoformat`, `last_day.isoformat`, `str`, `max`, `timezone.localdate`, `timedelta`



### `simulation_roster` — 135행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `request.GET.get`, `SimulationContext`, `context.roster`, `attach_comparisons`, `JsonResponse`, `PredictionUnavailable`, `history.append`, `range`, `context.recommended`, `str`



### `simulation_result` — 206행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `json.loads`, `JsonResponse`, `len`, `PredictionUnavailable`, `simulate`, `SimulationContext`, `str`

