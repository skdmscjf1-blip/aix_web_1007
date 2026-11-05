# `board/matchbot.py`

회원·게시글·댓글·신고



[실제 코드 열기](../../../board/matchbot.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import logging

from datetime import timedelta

from django.contrib.auth import get_user_model

from django.db import transaction

from django.utils import timezone

from .models import Match, Post, Profile

```

## 함수·클래스 안내

### `get_bot` — 24행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `get_user_model`, `User.objects.get_or_create`, `Profile.objects.get_or_create`, `user.set_unusable_password`, `user.save`



### `_leader` — 34행

입력 이름: `team`, `field`

읽을 때 따라갈 호출(중복 제외): `PlayerStats.objects.filter(player__team=team, season=SEASON, **{f'{field}__gt': 0}).select_related('player').order_by(f'-{field}').first`, `PlayerStats.objects.filter(player__team=team, season=SEASON, **{f'{field}__gt': 0}).select_related('player').order_by`, `getattr`, `PlayerStats.objects.filter(player__team=team, season=SEASON, **{f'{field}__gt': 0}).select_related`, `PlayerStats.objects.filter`



### `_brief` — 48행

입력 이름: `team`

읽을 때 따라갈 호출(중복 제외): `_leader`, `parts.append`, `' · '.join`



### `build_post` — 58행

입력 이름: `m`

읽을 때 따라갈 호출(중복 제외): `timezone.is_aware`, `timezone.localtime`, `_brief`, `k.weekday`



### `ensure_match_threads` — 75행

곧 열릴 경기 중 글이 아직 없는 경기에 글을 올림. 새로 올린 글 수를 돌려줌.

입력 이름: `days`

읽을 때 따라갈 호출(중복 제외): `timezone.now`, `list`, `Match.objects.filter(post__isnull=True, kickoff__gte=now, kickoff__lte=now + timedelta(days=days)).select_related`, `get_bot`, `transaction.atomic`, `build_post`, `Post.objects.create`, `Match.objects.filter(pk=m.pk, post__isnull=True).update`, `Match.objects.filter`, `post.delete`, `timedelta`



### `safe_ensure` — 97행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `ensure_match_threads`, `log.exception`

