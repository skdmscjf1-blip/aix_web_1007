# `player/tracking_demo_views.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../player/tracking_demo_views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

from django.conf import settings

from django.http import Http404

from django.shortcuts import render

from team.models import Team

from player.services import get_filtered_best11

```

## 함수·클래스 안내

### `connect_roster` — 13행

기존 BEST11을 가상 슬롯에 연결합니다.

입력 이름: `data`, `team`, `prefix`

읽을 때 따라갈 호출(중복 제외): `get_filtered_best11`, `slots.items`, `zip`, `demo_player.update`, `roster.append`, `str`, `len`, `assignments.append`, `set`



### `tracking_demo` — 81행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `Team.objects.all().order_by`, `request.GET.get`, `find_team`, `render`, `json.loads`, `teams.filter(pk=int(value)).first`, `warnings.append`, `connect_roster`, `target.read_text`, `Http404`, `Team.objects.all`, `value.isdecimal`, `' '.join`, `teams.filter`, `str`, `int`

