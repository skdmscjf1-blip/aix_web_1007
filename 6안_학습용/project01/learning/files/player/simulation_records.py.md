# `player/simulation_records.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../player/simulation_records.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.core.paginator import Paginator

from django.db.models import Q

from simulation.models import SimulationRun

from simulation.generator import VERSION

from simulation.tracking_models import SimulationPlayerTracking

from simulation.tracking_metrics import TRACKING_VERSION

from simulation.event_models import SimulationPlayerEventStats

from simulation.event_metrics import EVENT_VERSION

```

## 함수·클래스 안내

### `get_player_simulation_records` — 60행

입력 이름: `player_id`, `page_number`

찾아볼 반환 사전 키(분기·내부 함수 포함): `page`, `groups`

읽을 때 따라갈 호출(중복 제외): `SimulationPlayerTracking.objects.filter`, `SimulationPlayerEventStats.objects.filter`, `SimulationRun.objects.filter(generator_version=VERSION).filter(Q(pk__in=gps_query.values('run_id')) | Q(pk__in=event_query.values('run_id'))).order_by`, `Paginator(runs, 10).get_page`, `groups.append`, `SimulationRun.objects.filter(generator_version=VERSION).filter`, `Paginator`, `gps_query.filter`, `event_query.filter`, `records.get`, `run.document.get`, `rows.append`, `SimulationRun.objects.filter`, `Q`, `snapshot.get('home_team', {}).get`, `snapshot.get('away_team', {}).get`, `gps_query.values`, `event_query.values`, `snapshot.get`, `getattr`

