# `project01/urls.py`

프로젝트 실행 설정과 전체 URL — 주소와 처리 함수 연결



[실제 코드 열기](../../../project01/urls.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.contrib import admin

from django.urls import include, path

from django.conf import settings

from django.conf.urls.static import static

```

## 함수·클래스 안내