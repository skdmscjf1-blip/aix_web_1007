# `team/models.py`

구단 기록·기본 승무패 예측·라인업 실험 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../team/models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db import models

```

## 함수·클래스 안내

### `Team` — 7행

DB 필드:

- `team_name`: `models.CharField`

- `league`: `models.CharField`

- `stadium`: `models.CharField`

- `logo`: `models.ImageField`

클래스 안의 작업: `__str__`



### `MatchResult` — 19행

DB 필드:

- `match_date`: `models.DateField`

- `round`: `models.PositiveSmallIntegerField`

- `home_team_id`: `models.CharField`

- `away_team_id`: `models.CharField`

- `home_goals`: `models.PositiveSmallIntegerField`

- `away_goals`: `models.PositiveSmallIntegerField`

- `official_match_id`: `models.PositiveIntegerField`

- `updated_at`: `models.DateTimeField`

클래스 안의 작업: `clean`, `result`, `__str__`

