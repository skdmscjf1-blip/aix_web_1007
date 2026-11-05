# `simulation/event_models.py`

가상 경기 생성·검사·저장·선수별 지표 집계 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../simulation/event_models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db import models

```

## 함수·클래스 안내

### `SimulationPlayerEventStats` — 6행

DB 필드:

- `run`: `models.ForeignKey`

- `player`: `models.ForeignKey`

- `slot_id`: `models.CharField`

- `team_side`: `models.CharField`

- `data_source`: `models.CharField`

- `metrics_version`: `models.CharField`

- `parameters`: `models.JSONField`

- `pass_attempts`: `models.PositiveIntegerField`

- `successful_passes`: `models.PositiveIntegerField`

- `failed_passes`: `models.PositiveIntegerField`

- `passes_received`: `models.PositiveIntegerField`

- `forward_pass_attempts`: `models.PositiveIntegerField`

- `successful_forward_passes`: `models.PositiveIntegerField`

- `interceptions`: `models.PositiveIntegerField`

- `possession_seconds`: `models.FloatField`

클래스 안의 작업: `pass_success_rate`

