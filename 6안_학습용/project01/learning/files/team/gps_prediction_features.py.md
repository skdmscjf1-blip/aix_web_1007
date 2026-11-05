# `team/gps_prediction_features.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../team/gps_prediction_features.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from team.player_prediction_features import find_team

from simulation.models import SimulationRun

from simulation.generator import VERSION

from simulation.management.commands.export_match_features import build_row

```

## 함수·클래스 안내

### `build_gps_features` — 29행

입력 이름: `home_name`, `away_name`

찾아볼 반환 사전 키(분기·내부 함수 포함): `available`, `data_source`, `run_count`, `scenario_count`, `home_name`, `away_name`, `rows`, `values`, `message`

읽을 때 따라갈 호출(중복 제외): `find_team`, `SimulationRun.objects.filter(generator_version=VERSION, home_team=home, away_team=away).order_by`, `set`, `runs.iterator`, `rows.append`, `len`, `ValueError`, `samples.append`, `scenarios.add`, `SimulationRun.objects.filter`, `build_row`, `sum`

