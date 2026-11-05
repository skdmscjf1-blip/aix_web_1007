# `board/models.py`

회원·게시글·댓글·신고 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../board/models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.conf import settings

from django.db import models

from django.utils import timezone

```

## 함수·클래스 안내

### `Profile` — 11행

회원가입 때 받는 별명 (아이디·비밀번호는 Django 기본 User 사용)

DB 필드:

- `user`: `models.OneToOneField`

- `nickname`: `models.CharField`

- `created_at`: `models.DateTimeField`

클래스 안의 작업: `__str__`



### `_Moderated` — 22행

DB 필드:

- `status`: `models.CharField`

- `deleted_reason`: `models.CharField`

- `deleted_at`: `models.DateTimeField`

클래스 안의 작업: `soft_delete`, `restore`



### `Post` — 48행

DB 필드:

- `author`: `models.ForeignKey`

- `title`: `models.CharField`

- `content`: `models.TextField`

- `views`: `models.PositiveIntegerField`

- `created_at`: `models.DateTimeField`

- `updated_at`: `models.DateTimeField`

클래스 안의 작업: `__str__`



### `Comment` — 65행

DB 필드:

- `post`: `models.ForeignKey`

- `author`: `models.ForeignKey`

- `content`: `models.CharField`

- `created_at`: `models.DateTimeField`

클래스 안의 작업: `__str__`



### `Report` — 80행

신고. 서로 다른 회원 N명이 신고하면 자동 숨김 (views.REPORT_LIMIT)

DB 필드:

- `user`: `models.ForeignKey`

- `post`: `models.ForeignKey`

- `comment`: `models.ForeignKey`

- `reason`: `models.CharField`

- `created_at`: `models.DateTimeField`



### `BannedWord` — 96행

관리자가 추가하는 금칙어 / 허용어(오탐 방지). 기본 금칙어는 filters.py 에 들어 있음

DB 필드:

- `word`: `models.CharField`

- `allow`: `models.BooleanField`

- `created_at`: `models.DateTimeField`

클래스 안의 작업: `__str__`



### `Match` — 109행

예정된 경기. 경기 하루 이틀 전에 AI 해설위원이 "누가 이길까요?" 글을 자동으로 올림

DB 필드:

- `home`: `models.ForeignKey`

- `away`: `models.ForeignKey`

- `kickoff`: `models.DateTimeField`

- `post`: `models.OneToOneField`

- `created_at`: `models.DateTimeField`

클래스 안의 작업: `__str__`

