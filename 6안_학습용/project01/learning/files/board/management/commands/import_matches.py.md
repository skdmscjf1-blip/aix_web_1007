# `board/management/commands/import_matches.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../../../board/management/commands/import_matches.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import csv

import re

from datetime import datetime

from django.conf import settings

from django.core.management.base import BaseCommand, CommandError

from django.utils import timezone

from board.models import Match

from team.models import Team

```

## 함수·클래스 안내

### `_k` — 17행

입력 이름: `s`

읽을 때 따라갈 호출(중복 제외): `re.sub`, `(s or '').lower`



### `resolve` — 21행

입력 이름: `name`, `teams`

읽을 때 따라갈 호출(중복 제외): `_k`, `len`



### `Command` — 36행

클래스 안의 작업: `add_arguments`, `handle`



## 실행 전 확인

관리 명령은 DB나 파일을 쓸 수 있습니다. `handle()`과 옵션을 먼저 읽고 복사본에서 실행하세요. 문법 정리는 명령의 실제 쓰기 작업을 실행해 검증했다는 뜻이 아닙니다.