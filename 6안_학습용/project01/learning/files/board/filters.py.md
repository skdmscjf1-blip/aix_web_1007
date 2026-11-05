# `board/filters.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../board/filters.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import re

import unicodedata

```

## 함수·클래스 안내

### `normalize` — 103행

입력 이름: `text`

읽을 때 따라갈 호출(중복 제외): `''.join((c if 'ㄱ' <= c <= 'ㅣ' else unicodedata.normalize('NFKC', c) for c in text or '')).lower`, `re.sub`, `''.join`, `unicodedata.normalize`



### `Matcher` — 114행

클래스 안의 작업: `__init__`, `find`



### `get_matcher` — 142행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `list`, `Matcher`, `BannedWord.objects.values_list`



### `scan_all` — 149행

이미 올라온 글·댓글을 모두 검사해서 위반이면 숨김 처리. (글 수, 댓글 수) 반환

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `get_matcher`, `Post.objects.filter`, `Comment.objects.filter`, `m.find`, `p.soft_delete`, `c.soft_delete`

