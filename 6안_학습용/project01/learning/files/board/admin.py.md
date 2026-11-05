# `board/admin.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../board/admin.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.contrib import admin, messages

from .filters import scan_all

from .models import BannedWord, Comment, Match, Post, Profile, Report

```

## 함수·클래스 안내

### `hide` — 11행

입력 이름: `modeladmin`, `request`, `queryset`

읽을 때 따라갈 호출(중복 제외): `admin.action`, `o.soft_delete`, `request.user.get_username`



### `restore` — 17행

입력 이름: `modeladmin`, `request`, `queryset`

읽을 때 따라갈 호출(중복 제외): `admin.action`, `o.restore`



### `rescan` — 23행

입력 이름: `modeladmin`, `request`, `queryset`

읽을 때 따라갈 호출(중복 제외): `admin.action`, `scan_all`, `messages.info`



### `PostAdmin` — 29행



### `CommentAdmin` — 45행



### `BannedWordAdmin` — 61행



### `MatchAdmin` — 71행

