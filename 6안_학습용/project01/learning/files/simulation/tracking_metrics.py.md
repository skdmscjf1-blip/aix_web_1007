# `simulation/tracking_metrics.py`

좌표 두 장면의 차이로 거리·속도를 구해 선수별 합산



[실제 코드 열기](../../../simulation/tracking_metrics.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import math

from itertools import groupby

from .tracking_spatial import SPATIAL_PARAMETERS, extract_spatial

from .generator import check_document

```

## 함수·클래스 안내

### `measure_segments` — 21행

이동 구간 목록을 합산합니다. 항목 순서는 (거리 m, 시간 초, 속도 km/h)입니다.

입력 이름: `segments`

찾아볼 반환 사전 키(분기·내부 함수 포함): `tracked_seconds`, `total_distance_m`, `distance_per_minute`, `avg_speed_kmh`, `max_speed_kmh`, `high_speed_distance_m`, `sprint_count`, `sprint_distance_m`, `sprint_seconds`

읽을 때 따라갈 호출(중복 제외): `sum`, `groupby`, `ValueError`, `list`, `round`, `max`



### `extract_player_tracking` — 86행

연속된 두 장면의 위치 차이를 선수별 이동 구간으로 바꿉니다.

document는 경기 조건·명단·시간별 좌표가 담긴 사전(dict)입니다.
이 함수는 계산만 하며, DB 저장은 관리 명령어에서 담당합니다.

입력 이름: `document`

읽을 때 따라갈 호출(중복 제외): `check_document`, `zip`, `extract_spatial`, `segments.items`, `document.get`, `ValueError`, `measure_segments`, `abs`, `math.hypot`, `segments[player_id].append`

