# `team/player_comparison.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../team/player_comparison.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import math

from player.gk_evaluation import match_record

from player.models import PlayerStats

from player.services import get_formation_candidates

```

## 함수·클래스 안내

### `raw_value` — 136행

실제 기록을 반환합니다. 미확인 기록은 None입니다.

입력 이름: `stats`, `axis`, `snapshot`

읽을 때 따라갈 호출(중복 제외): `float`, `match_record`, `getattr`, `math.isfinite`



### `comparable_value` — 179행

그래프에서 바깥쪽일수록 높은 평가가 되도록 변환합니다.

입력 이름: `value`, `key`



### `attach_comparisons` — 193행

선수 명단에 자리별 비교 데이터를 추가한 사본을 반환합니다.

입력 이름: `context`, `official_id`, `roster`

읽을 때 따라갈 호출(중복 제외): `get_formation_candidates`, `AXES.items`, `list`, `set`, `len`, `PlayerStats.objects.filter(season=2026, player__team=context.db_teams[official_id]).select_related`, `result.append`, `max`, `duplicates.add`, `by_id.get`, `comparable_value`, `PlayerStats.objects.filter`, `raw_value`, `axes.append`, `(stats.player.position or '').strip().upper`, `min`, `(stats.player.position or '').strip`, `round`

