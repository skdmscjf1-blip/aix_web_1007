# `validate_tracking_demo.py`

프로젝트 실행 도구



[실제 코드 열기](../../validate_tracking_demo.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

import math

from pathlib import Path

```

## 함수·클래스 안내

### `validate` — 8행

입력 이름: `data`

읽을 때 따라갈 호출(중복 제외): `set`, `check`, `enumerate`, `sum`, `len`, `positions.items`, `frame_lookup.get`, `errors.append`, `math.isfinite`, `in_pitch`, `round`, `previous_positions.get`, `max`, `math.hypot`, `event.get`, `close`, `abs`



### `main` — 219행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `print`, `json.loads`, `validate`, `target.read_text`, `len`, `Path(__file__).resolve`, `Path`

