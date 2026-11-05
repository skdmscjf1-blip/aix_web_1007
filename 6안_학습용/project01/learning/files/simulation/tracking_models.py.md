# `simulation/tracking_models.py`

가상 경기 생성·검사·저장·선수별 지표 집계 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../simulation/tracking_models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db import models

```

## 함수·클래스 안내

### `SimulationPlayerTracking` — 6행

DB 필드:

- `run`: `models.ForeignKey`

- `player`: `models.ForeignKey`

- `slot_id`: `models.CharField`

- `team_side`: `models.CharField`

- `data_source`: `models.CharField`

- `metrics_version`: `models.CharField`

- `parameters`: `models.JSONField`

- `tracked_seconds`: `models.FloatField`

- `total_distance_m`: `models.FloatField`

- `distance_per_minute`: `models.FloatField`

- `avg_speed_kmh`: `models.FloatField`

- `max_speed_kmh`: `models.FloatField`

- `high_speed_distance_m`: `models.FloatField`

- `sprint_count`: `models.PositiveIntegerField`

- `sprint_distance_m`: `models.FloatField`

- `sprint_seconds`: `models.FloatField`

- `average_x`: `models.FloatField`

- `average_y`: `models.FloatField`

- `defensive_third_seconds`: `models.FloatField`

- `middle_third_seconds`: `models.FloatField`

- `attacking_third_seconds`: `models.FloatField`

- `opponent_box_entries`: `models.PositiveIntegerField`

