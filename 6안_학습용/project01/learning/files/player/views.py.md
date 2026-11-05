# `player/views.py`

선수 조회·공통 평가·BEST11·연구실 — 요청 처리와 응답 연결



[실제 코드 열기](../../../player/views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from player.simulation_summary import attach_simulation_summaries

from player.simulation_records import get_player_simulation_records

from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse

from player.models import Player, PlayerStats

from team.models import Team

from player.services import get_best11, get_player_radar, get_filtered_best11, get_formations

```

## 함수·클래스 안내

### `plist` — 24행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `request.GET.get`, `Player.objects.select_related('team').all`, `qs.order_by`, `Team.objects.all().order_by`, `render`, `qs.filter`, `attach_simulation_summaries`, `Player.objects.select_related`, `Team.objects.all`



### `pview` — 74행

입력 이름: `request`, `id`

읽을 때 따라갈 호출(중복 제외): `get_object_or_404`, `PlayerStats.objects.filter(player=player).order_by`, `get_player_simulation_records`, `render`, `PlayerStats.objects.filter`, `request.GET.get`



### `best11` — 112행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `request.GET.get`, `get_filtered_best11`, `Team.objects.all().order_by`, `get_formations`, `render`, `Team.objects.filter(id=result['team_id']).first`, `Team.objects.all`, `Team.objects.filter`



### `player_info` — 215행

입력 이름: `request`, `id`

읽을 때 따라갈 호출(중복 제외): `get_player_radar`, `JsonResponse`

