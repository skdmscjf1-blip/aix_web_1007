# `board/urls.py`

회원·게시글·댓글·신고 — 주소와 처리 함수 연결



[실제 코드 열기](../../../board/urls.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.contrib.auth.views import LogoutView

from django.urls import path

from django.urls import reverse_lazy

from . import views

```

## 함수·클래스 안내