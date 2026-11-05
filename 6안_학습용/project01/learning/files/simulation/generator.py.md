# `simulation/generator.py`

시나리오와 시드로 22명·공·패스 장면을 생성



[실제 코드 열기](../../../simulation/generator.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import copy

import hashlib

import json

import math

import random

from player.tracking_demo_views import connect_roster

from validate_tracking_demo import validate

```

## 함수·클래스 안내

### `digest` — 130행

입력 이름: `value`

읽을 때 따라갈 호출(중복 제외): `json.dumps`, `hashlib.sha256(raw.encode('utf-8')).hexdigest`, `hashlib.sha256`, `raw.encode`



### `check_document` — 141행

입력 이름: `document`

찾아볼 반환 사전 키(분기·내부 함수 포함): `passed`, `maximum_speed_mps`, `validator`

읽을 때 따라갈 호출(중복 제외): `validate`, `ValueError`, `round`, `'; '.join`



### `generate` — 159행

입력 이름: `source`, `scenario`, `home`, `away`, `seed`, `source_hash`

찾아볼 반환 사전 키(분기·내부 함수 포함): `x`, `y`

읽을 때 따라갈 호출(중복 제외): `copy.deepcopy`, `random.Random`, `rng.choice`, `list`, `record`, `data.update`, `player.update`, `connect_roster`, `math.hypot`, `frames.append`, `groups.items`, `range`, `max`, `advance`, `min`, `events.append`, `targets`, `check_document`, `ValueError`, `round`, `distance`, `math.exp`, `weights.append`, `rng.choices`, `int`, `len`, `point`, `pid.endswith`

