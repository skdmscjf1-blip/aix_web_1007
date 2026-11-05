# `manager/backup.py`

DB와 관련 데이터를 보관하고 복원하는 도구



[실제 코드 열기](../../../manager/backup.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

import re

import sqlite3

import time

from pathlib import Path

```

## 함수·클래스 안내

### `make_backup` — 14행

입력 이름: `db_path`, `folder`, `reason`, `batch_id`, `user`

읽을 때 따라갈 호출(중복 제외): `Path`, `folder.mkdir`, `time.strftime`, `path.exists`, `sqlite3.connect`, `dict`, `path.with_suffix('.json').write_text`, `_prune`, `str`, `src.backup`, `dst.close`, `src.close`, `json.dumps`, `path.with_suffix`, `path.stat`



### `list_backups` — 44행

입력 이름: `folder`

읽을 때 따라갈 호출(중복 제외): `Path`, `sorted`, `folder.exists`, `folder.glob`, `p.with_suffix`, `mp.exists`, `out.append`, `NAME_RE.match`, `dict`, `json.loads`, `mp.read_text`, `p.stat`, `meta.get`



### `get_backup` — 69행

입력 이름: `folder`, `name`

읽을 때 따라갈 호출(중복 제외): `list_backups`, `NAME_RE.match`



### `restore_backup` — 78행

name 시점으로 DB 복원. 복원 직전 상태를 먼저 자동 백업한다.

입력 이름: `db_path`, `folder`, `name`, `user`

읽을 때 따라갈 호출(중복 제외): `make_backup`, `sqlite3.connect`, `get_backup`, `ValueError`, `str`, `bk.backup`, `live.close`, `bk.close`, `Path`



### `_prune` — 95행

입력 이름: `folder`

읽을 때 따라갈 호출(중복 제외): `sorted`, `p.unlink`, `p.with_suffix('.json').unlink`, `Path(folder).glob`, `NAME_RE.match`, `p.with_suffix`, `Path`

