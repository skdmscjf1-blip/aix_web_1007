# `board/templatetags/board_tags.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../../board/templatetags/board_tags.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django import template

from board.models import Post

```

## 함수·클래스 안내

### `nick` — 15행

입력 이름: `user`

읽을 때 따라갈 호출(중복 제외): `user.get_username`



### `who` — 23행

화면에 보이는 작성자 표기: 별명(abc****)  — 아이디는 앞 3자리만, 나머지는 *

입력 이름: `user`

읽을 때 따라갈 호출(중복 제외): `user.get_username`, `max`, `len`



### `latest_posts` — 39행

입력 이름: `count`

찾아볼 반환 사전 키(분기·내부 함수 포함): `posts`

읽을 때 따라갈 호출(중복 제외): `register.inclusion_tag`, `Post.objects.filter(status=Post.OK).select_related`, `Post.objects.filter`

