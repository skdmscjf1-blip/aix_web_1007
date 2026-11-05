# `team/virtual_stats.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../team/virtual_stats.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

import math

import random

from datetime import datetime

from pathlib import Path

from django.conf import settings

```

## 함수·클래스 안내

### `path` — 49행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `Path`



### `player_age` — 53행

나이. DB의 age 칸이 비어 있어(0) 생년월일로 계산한다. 기준일은 시즌 말(2026-11-01).

입력 이름: `player`, `on`

읽을 때 따라갈 호출(중복 제외): `date`



### `_clamp` — 64행

입력 이름: `v`, `lo`, `hi`

읽을 때 따라갈 호출(중복 제외): `max`, `min`



### `team_conceded_per_game` — 68행

실제 구단 실점 / 경기 (구단성적.json). 골키퍼 가상 실점의 기준으로만 쓴다.

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `json.loads`, `isinstance`, `next`, `''.join((ch for ch in str(r.get('순위', '')) if not ch.isdigit())).strip`, `f.read_text`, `''.join`, `int`, `Path`, `doc.values`, `str`, `r.get`, `ch.isdigit`



### `build` — 92행

선수별 가상 기록을 만든다 (DB는 읽기만 한다).

입력 이름: 

찾아볼 반환 사전 키(분기·내부 함수 포함): `virtual`, `note`, `seed`, `season`, `generated_at`, `players`

읽을 때 따라갈 호출(중복 제외): `team_conceded_per_game`, `PlayerStats.objects.filter(season=2026, minutes__gt=0).select_related`, `(s.player.position or '').strip().upper`, `random.Random`, `max`, `datetime.now().isoformat`, `sum`, `len`, `PlayerStats.objects.filter`, `player_age`, `round`, `conceded.get`, `_clamp`, `d.update`, `str`, `conceded.values`, `(s.player.position or '').strip`, `TEAM_SHORT.get`, `datetime.now`, `rng.gauss`, `math.exp`, `min`, `rng.uniform`



### `save` — 165행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `build`, `path`, `p.parent.mkdir`, `p.write_text`, `_cache.clear`, `json.dumps`



### `load` — 174행

저장된 가상 데이터. 파일이 없으면 같은 규칙으로 바로 만든다(저장은 안 함).

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `path`, `_cache.update`, `build`, `p.stat`, `_cache.get`, `json.loads`, `isinstance`, `p.read_text`, `data.get`



### `for_player` — 195행

입력 이름: `player_id`

읽을 때 따라갈 호출(중복 제외): `load()['players'].get`, `str`, `load`

