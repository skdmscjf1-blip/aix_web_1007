# `board/signals.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../board/signals.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db.models.signals import post_save

from django.dispatch import receiver

from .filters import scan_all

from .models import BannedWord

```

## 함수·클래스 안내

### `rescan_after_new_word` — 11행

금칙어를 추가하면 기존 글·댓글도 바로 다시 검사 (자동 삭제)

입력 이름: `sender`, `instance`

읽을 때 따라갈 호출(중복 제외): `receiver`, `scan_all`

