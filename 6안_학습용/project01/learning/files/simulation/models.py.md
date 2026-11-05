# `simulation/models.py`

가상 경기 생성·검사·저장·선수별 지표 집계 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../simulation/models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import uuid

from django.core.exceptions import ValidationError

from django.db import models

from .tracking_models import SimulationPlayerTracking

from .event_models import SimulationPlayerEventStats

```

## 함수·클래스 안내

### `SimulationRun` — 10행

DB 필드:

- `id`: `models.UUIDField`

- `created_at`: `models.DateTimeField`

- `home_team`: `models.ForeignKey`

- `away_team`: `models.ForeignKey`

- `scenario_code`: `models.CharField`

- `scenario_name`: `models.CharField`

- `generator_version`: `models.CharField`

- `seed`: `models.PositiveIntegerField`

- `duration_sec`: `models.FloatField`

- `frame_count`: `models.PositiveIntegerField`

- `event_count`: `models.PositiveIntegerField`

- `source_sha256`: `models.CharField`

- `fingerprint`: `models.CharField`

- `document`: `models.JSONField`

- `parameters`: `models.JSONField`

- `validation`: `models.JSONField`

클래스 안의 작업: `clean`, `__str__`



### `SimulationTeamSummary` — 129행

DB 필드:

- `run`: `models.ForeignKey`

- `side`: `models.CharField`

- `metrics_version`: `models.CharField`

- `distance_m`: `models.FloatField`

- `pass_attempts`: `models.PositiveIntegerField`

- `successful_passes`: `models.PositiveIntegerField`

- `interceptions`: `models.PositiveIntegerField`

- `possession_seconds`: `models.FloatField`

- `updated_at`: `models.DateTimeField`

클래스 안의 작업: `pass_success_rate`

