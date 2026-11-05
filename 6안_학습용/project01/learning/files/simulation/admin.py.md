# `simulation/admin.py`

가상 경기 생성·검사·저장·선수별 지표 집계



[실제 코드 열기](../../../simulation/admin.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.contrib import admin

from django.core.exceptions import PermissionDenied

from django.http import Http404, JsonResponse

from django.urls import path, reverse

from django.utils.html import format_html

from .models import SimulationRun, SimulationTeamSummary

from . import tracking_admin

from . import event_admin

```

## 함수·클래스 안내

### `SimulationRunAdmin` — 14행

클래스 안의 작업: `has_add_permission`, `has_change_permission`, `has_delete_permission`, `validation_status`, `roster_snapshot`, `replay_link`, `download_link`, `get_urls`, `download`



### `SimulationTeamSummaryAdmin` — 172행

클래스 안의 작업: `success_rate`, `has_add_permission`, `has_change_permission`, `has_delete_permission`

