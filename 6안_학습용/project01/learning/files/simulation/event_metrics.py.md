# `simulation/event_metrics.py`

공 소유와 생성된 패스 이벤트를 선수별 통계로 집계



[실제 코드 열기](../../../simulation/event_metrics.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import math

from .generator import check_document

```

## 함수·클래스 안내

### `extract_player_events` — 17행

입력 이름: `document`

읽을 때 따라갈 호출(중복 제외): `check_document`, `document.get`, `sorted`, `result.values`, `ValueError`, `round`, `len`, `event.get`, `int`, `math.hypot`

