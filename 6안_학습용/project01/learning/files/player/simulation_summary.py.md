# `player/simulation_summary.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../player/simulation_summary.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db.models import Count, Max, Q, Sum

from simulation.generator import VERSION

from simulation.tracking_metrics import TRACKING_VERSION

from simulation.tracking_models import SimulationPlayerTracking

from simulation.event_metrics import EVENT_VERSION

from simulation.event_models import SimulationPlayerEventStats

```

## 함수·클래스 안내

### `ratio` — 12행

입력 이름: `numerator`, `denominator`, `multiplier`



### `attach_simulation_summaries` — 19행

입력 이름: `players`

읽을 때 따라갈 호출(중복 제외): `list`, `SimulationPlayerTracking.objects.filter(player_id__in=ids, metrics_version=TRACKING_VERSION, data_source='synthetic', run__generator_version=VERSION).values('player_id').annotate`, `SimulationPlayerEventStats.objects.filter(player_id__in=ids, metrics_version=EVENT_VERSION, data_source='synthetic', run__generator_version=VERSION).values('player_id').annotate`, `gps.get`, `events.get`, `SimulationPlayerTracking.objects.filter(player_id__in=ids, metrics_version=TRACKING_VERSION, data_source='synthetic', run__generator_version=VERSION).values`, `Count`, `Sum`, `Max`, `SimulationPlayerEventStats.objects.filter(player_id__in=ids, metrics_version=EVENT_VERSION, data_source='synthetic', run__generator_version=VERSION).values`, `g.get`, `e.get`, `bool`, `ratio`, `SimulationPlayerTracking.objects.filter`, `Q`, `SimulationPlayerEventStats.objects.filter`

