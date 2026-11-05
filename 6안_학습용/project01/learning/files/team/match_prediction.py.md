# `team/match_prediction.py`

대상 경기 전 팀 기록으로 특징을 만들고 예측 모델의 세 확률 계산



[실제 코드 열기](../../../team/match_prediction.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from datetime import date

from hashlib import sha256

import json

import math

from pathlib import Path

from django.conf import settings

```

## 함수·클래스 안내

### `PredictionUnavailable` — 42행



### `data_path` — 46행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `Path`



### `model_path` — 54행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `Path`



### `_load_json_matches` — 58행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `document.get`, `set`, `sorted`, `data_path().read_bytes`, `json.loads`, `PredictionUnavailable`, `seen.add`, `sha256(raw).hexdigest`, `date.fromisoformat`, `data_path`, `sha256`, `type`, `min`



### `team_options` — 111행

입력 이름: `matches`

읽을 때 따라갈 호출(중복 제외): `sorted`, `teams.items`



### `team_history` — 127행

입력 이름: `matches`, `team_id`, `before`

읽을 때 따라갈 호출(중복 제외): `sorted`, `history.append`, `date.fromisoformat`



### `averages` — 157행

입력 이름: `rows`

읽을 때 따라갈 호출(중복 제외): `sum`, `len`



### `features_for` — 164행

입력 이름: `matches`, `home_id`, `away_id`, `before`

읽을 때 따라갈 호출(중복 제외): `any`, `zip`, `values.append`, `PredictionUnavailable`, `team_history`, `summaries.append`, `blended.append`, `sum`, `max`, `min`, `len`, `averages`, `date.fromisoformat`



### `training_rows` — 277행

입력 이름: `matches`

읽을 때 따라갈 호출(중복 제외): `date.fromisoformat`, `rows.append`, `features_for`



### `chronological_split` — 305행

입력 이름: `rows`

읽을 때 따라갈 호출(중복 제외): `len`, `PredictionUnavailable`, `int`, `set`



### `poisson_probabilities` — 326행

예상 득점으로 0~25골의 스코어 확률을 만들고 승·무·패로 합칩니다.

입력 이름: `home_rate`, `away_rate`

읽을 때 따라갈 호출(중복 제외): `range`, `enumerate`, `sum`, `probabilities.items`, `math.exp`, `home.append`, `away.append`, `probabilities.values`, `PredictionUnavailable`, `math.isfinite`



### `predict_probabilities` — 358행

입력 이름: `bundle`, `features`

읽을 때 따라갈 호출(중복 제외): `sum`, `dict`, `model.get`, `poisson_probabilities`, `math.exp`, `zip`, `max`



### `load_bundle` — 405행

입력 이름: `dataset_hash`

읽을 때 따라갈 호출(중복 제외): `json.loads`, `date.fromisoformat`, `PredictionUnavailable`, `model_path().read_text`, `model.get`, `set`, `len`, `all`, `model_path`, `math.isfinite`



### `forecast` — 463행

입력 이름: `matches`, `bundle`, `home_id`, `away_id`, `target_date`

찾아볼 반환 사전 키(분기·내부 함수 포함): `home_name`, `away_name`, `date`, `probabilities`, `best_label`, `home`, `away`, `stale_days`, `long_gap`, `expected_home_goals`, `expected_away_goals`, `model_kind`

읽을 때 따라갈 호출(중복 제외): `date.fromisoformat`, `features_for`, `predict_probabilities`, `sorted`, `max`, `PredictionUnavailable`, `int`, `sum`, `target_date.isoformat`, `bundle['model'].get`, `team_options`, `units.values`



### `load_matches` — 541행

기존 JSON과 admin 입력 결과를 합쳐 예측에 사용합니다.

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `_load_json_matches`, `sorted`, `fixture`, `len`, `PredictionUnavailable`, `list`, `original_fixtures.get`, `by_fixture.get`, `by_fixture.values`, `canonical`, `sha256(json.dumps(canonical(matches), ensure_ascii=False).encode('utf-8')).hexdigest`, `MatchResult.objects.all`, `row.match_date.isoformat`, `by_fixture.pop`, `row.get_home_team_id_display`, `row.get_away_team_id_display`, `set`, `previous.get`, `tuple`, `sha256`, `json.dumps(canonical(matches), ensure_ascii=False).encode`, `json.dumps`

