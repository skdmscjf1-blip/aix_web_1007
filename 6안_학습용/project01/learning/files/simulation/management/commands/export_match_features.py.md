# `simulation/management/commands/export_match_features.py`

가상 경기 생성·검사·저장·선수별 지표 집계



[실제 코드 열기](../../../../../simulation/management/commands/export_match_features.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import csv

import os

import tempfile

from pathlib import Path

from django.conf import settings

from django.core.management.base import BaseCommand, CommandError

from simulation.models import SimulationRun

from simulation.generator import VERSION

from simulation.tracking_models import SimulationPlayerTracking

from simulation.tracking_metrics import TRACKING_VERSION

from simulation.event_models import SimulationPlayerEventStats

from simulation.event_metrics import EVENT_VERSION

```

## 함수·클래스 안내

### `percentage` — 51행

입력 이름: `numerator`, `denominator`



### `build_row` — 58행

입력 이름: `run`

읽을 때 따라갈 호출(중복 제외): `sum`, `grouped.items`, `document.get`, `ValueError`, `p.get`, `any`, `str`, `snapshot.get('home_team', {}).get`, `snapshot.get('away_team', {}).get`, `len`, `SimulationPlayerTracking.objects.filter`, `SimulationPlayerEventStats.objects.filter`, `set`, `max`, `percentage`, `round`, `grouped.values`, `snapshot.get`, `abs`



### `Command` — 184행

클래스 안의 작업: `add_arguments`, `handle`



## 실행 전 확인

관리 명령은 DB나 파일을 쓸 수 있습니다. `handle()`과 옵션을 먼저 읽고 복사본에서 실행하세요. 문법 정리는 명령의 실제 쓰기 작업을 실행해 검증했다는 뜻이 아닙니다.