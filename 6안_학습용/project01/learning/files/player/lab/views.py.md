# `player/lab/views.py`

선수 조회·공통 평가·BEST11·연구실 — 요청 처리와 응답 연결



[실제 코드 열기](../../../../player/lab/views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

from django.http import JsonResponse

from django.views.decorators.http import require_POST

from . import service

```

## 함수·클래스 안내

### `_body` — 14행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `json.loads`, `request.body.decode`



### `_wrap` — 21행

입력 이름: `fn`

읽을 때 따라갈 호출(중복 제외): `JsonResponse`, `fn`, `_body`

