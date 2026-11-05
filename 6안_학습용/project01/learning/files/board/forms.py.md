# `board/forms.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../board/forms.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import re

from django import forms

from django.contrib.auth import get_user_model

from django.db import transaction

from .filters import get_matcher

from .models import Comment, Post, Profile

```

## 함수·클래스 안내

### `SignupForm` — 18행

클래스 안의 작업: `clean_username`, `clean_nickname`, `clean_password1`, `clean`, `save`



### `_check_words` — 92행

입력 이름: `value`, `what`

읽을 때 따라갈 호출(중복 제외): `get_matcher().find`, `forms.ValidationError`, `get_matcher`



### `PostForm` — 100행

클래스 안의 작업: `clean_title`, `clean_content`



### `CommentForm` — 130행

클래스 안의 작업: `clean_content`

