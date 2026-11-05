# `manager/models.py`

관리자 입력 검토·반영·백업·기본 설정 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../manager/models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db import models

```

## 함수·클래스 안내

### `ImportBatch` — 7행

업로드 1회 = 1건. 점검 결과(plan)와 반영 결과를 보관한다.

DB 필드:

- `created_at`: `models.DateTimeField`

- `created_by`: `models.CharField`

- `filenames`: `models.TextField`

- `season`: `models.IntegerField`

- `status`: `models.CharField`

- `plan`: `models.JSONField`

- `result`: `models.JSONField`

- `schema_file`: `models.CharField`

클래스 안의 작업: `__str__`



### `StatColumn` — 28행

승인된 추가 컬럼 목록 (DB 구조에 없던 새 항목). 한 번 승인되면 다음 업로드부터는 묻지 않고 저장한다.

DB 필드:

- `name`: `models.CharField`

- `kind`: `models.CharField`

- `approved_at`: `models.DateTimeField`

- `batch`: `models.ForeignKey`

클래스 안의 작업: `__str__`



### `ExtraStat` — 42행

승인된 추가 컬럼 값을 선수·시즌별로 저장

DB 필드:

- `player`: `models.ForeignKey`

- `season`: `models.IntegerField`

- `data`: `models.JSONField`

클래스 안의 작업: `__str__`



### `ScoreConfig` — 56행

점수 기준 설정 (1건만 사용): 가중치, 최소 출전시간, 제외 선수 관리 여부

DB 필드:

- `data`: `models.JSONField`

- `updated_at`: `models.DateTimeField`



### `ScoreConfigLog` — 63행

점수 기준을 바꾼 기록 (누가, 언제, 무엇을)

DB 필드:

- `created_at`: `models.DateTimeField`

- `created_by`: `models.CharField`

- `summary`: `models.CharField`

- `before`: `models.JSONField`

- `after`: `models.JSONField`



### `BestExclusion` — 76행

BEST11 계산에서 제외할 선수

DB 필드:

- `player`: `models.OneToOneField`

- `reason`: `models.CharField`

- `snapshot`: `models.CharField`

- `created_at`: `models.DateTimeField`

- `created_by`: `models.CharField`

클래스 안의 작업: `__str__`

