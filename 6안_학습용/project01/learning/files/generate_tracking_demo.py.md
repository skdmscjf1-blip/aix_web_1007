# `generate_tracking_demo.py`

프로젝트 실행 도구



[실제 코드 열기](../../generate_tracking_demo.py)



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

### `position` — 47행

기본 위치 주변을 천천히 움직이는 가상 좌표.

입력 이름: `player_id`, `time`

찾아볼 반환 사전 키(분기·내부 함수 포함): `x`, `y`

읽을 때 따라갈 호출(중복 제외): `next`, `round`, `math.sin`



### `ball_position` — 70행

패스 전후에는 소유 선수를 따르고, 패스 중에는 이동.

입력 이름: `time`

찾아볼 반환 사전 키(분기·내부 함수 포함): `x`, `y`

읽을 때 따라갈 호출(중복 제외): `position`, `round`

