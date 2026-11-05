# `player/gk_evaluation.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../player/gk_evaluation.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

from pathlib import Path

from django.conf import settings

```

## 함수·클래스 안내

### `load_snapshot` — 33행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `snapshot.get`, `json.loads`, `isinstance`, `all`, `path.read_text`, `Path`



### `match_record` — 59행

입력 이름: `stats`, `snapshot`

읽을 때 따라갈 호출(중복 제외): `TEAM_NAMES.get`, `len`, `row.get`, `all`, `type`



### `official_metrics` — 99행

입력 이름: `stats`, `record`

찾아볼 반환 사전 키(분기·내부 함수 포함): `conceding`, `clean_sheet_rate`, `rating`

읽을 때 따라갈 호출(중복 제외): `float`



### `evaluation_status` — 107행

입력 이름: `stats_list`

찾아볼 반환 사전 키(분기·내부 함수 포함): `available`, `retrieved_at`, `source_url`

읽을 때 따라갈 호출(중복 제외): `load_snapshot`, `bool`, `all`, `snapshot.get`, `match_record`

