# `simulation/generator_backup.py`

가상 경기 생성·검사·저장·선수별 지표 집계



[실제 코드 열기](../../../simulation/generator_backup.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import copy

import hashlib

import json

import random

from player.tracking_demo_views import connect_roster

from validate_tracking_demo import validate

```

## 함수·클래스 안내

### `digest` — 91행

데이터 내용을 일정한 문자열로 바꿔 중복 검사값을 만듭니다.

입력 이름: `value`

읽을 때 따라갈 호출(중복 제외): `json.dumps`, `hashlib.sha256(raw.encode('utf-8')).hexdigest`, `hashlib.sha256`, `raw.encode`



### `check_document` — 104행

기존 검사 함수로 선수·시간·패스 위치 연결을 확인합니다.

입력 이름: `document`

찾아볼 반환 사전 키(분기·내부 함수 포함): `passed`, `maximum_speed_mps`, `validator`

읽을 때 따라갈 호출(중복 제외): `validate`, `ValueError`, `round`, `'; '.join`



### `generate` — 122행

참조 장면을 복사해서 한 개의 가상 경기 문서를 만듭니다.

입력 이름: `source`, `scenario`, `home`, `away`, `seed`, `source_hash`

찾아볼 반환 사전 키(분기·내부 함수 포함): `x`, `y`

읽을 때 따라갈 호출(중복 제외): `copy.deepcopy`, `bool`, `random.Random`, `round`, `change_time`, `document['players'].sort`, `check_document`, `scenario.get`, `rng.uniform`, `change_player_id`, `frame['ball'].update`, `connect_roster`, `value.startswith`, `ValueError`, `change_point`, `player.update`, `len`

