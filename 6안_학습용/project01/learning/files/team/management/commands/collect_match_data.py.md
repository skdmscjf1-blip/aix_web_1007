# `team/management/commands/collect_match_data.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../../../team/management/commands/collect_match_data.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from collections import Counter

from concurrent.futures import ThreadPoolExecutor, as_completed

from datetime import datetime, timedelta, timezone

import json

from pathlib import Path

import shutil

from urllib.error import URLError

from urllib.request import Request, urlopen

from django.core.management.base import BaseCommand, CommandError

from team.match_prediction import data_path

```

## 함수·클래스 안내

### `fetch_month` — 45행

입력 이름: `month`

읽을 때 따라갈 호출(중복 제외): `Request`, `document.get`, `urlopen`, `json.loads`, `ValueError`, `json.dumps(payload).encode`, `response.read`, `isinstance`, `str`, `data.get`, `json.dumps`



### `normalize_schedule` — 81행

입력 이름: `documents`

읽을 때 따라갈 호출(중복 제외): `timezone`, `sorted`, `Counter`, `set`, `range`, `timedelta`, `by_id.values`, `len`, `ValueError`, `team_counts.update`, `fixtures.add`, `any`, `row.get`, `datetime.strptime(row['gameDate'] + ' ' + row['gameTime'], '%Y.%m.%d %H:%M').replace`, `tuple`, `isinstance`, `str`, `type`, `kickoff.date().isoformat`, `kickoff.isoformat`, `all`, `min`, `datetime.strptime`, `datetime.now`, `pair_counts.values`, `kickoff.date`



### `save_schedule` — 257행

입력 이름: `matches`, `documents`, `target`

읽을 때 따라갈 호출(중복 제외): `Path`, `datetime.now`, `now.strftime`, `target.exists`, `target.parent.mkdir`, `source.write_text`, `target.with_suffix`, `temporary.write_text`, `temporary.replace`, `json.loads`, `previous.get`, `list`, `len`, `now.isoformat`, `target.with_name`, `shutil.copy2`, `target.read_text`, `sorted`, `json.dumps`, `match.get`



### `Command` — 356행

클래스 안의 작업: `handle`



## 실행 전 확인

관리 명령은 DB나 파일을 쓸 수 있습니다. `handle()`과 옵션을 먼저 읽고 복사본에서 실행하세요. 문법 정리는 명령의 실제 쓰기 작업을 실행해 검증했다는 뜻이 아닙니다.