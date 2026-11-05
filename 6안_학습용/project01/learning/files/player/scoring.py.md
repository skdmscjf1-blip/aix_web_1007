# `player/scoring.py`

평가 항목과 범주를 정의하고 숫자를 같은 눈금으로 바꾸는 공통 계산표



[실제 코드 열기](../../../player/scoring.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import math

```

## 함수·클래스 안내

### `_p90` — 20행

90분당 기록. 예: 5골 / 900분 * 90 = 0.5골.

입력 이름: `value`, `minutes`



### `_rate` — 29행

시도 수가 기준 이상일 때만 성공 비율(0~1)을 계산합니다.

입력 이름: `success`, `attempt`, `minimum`



### `_full_match_rate` — 36행

총 출전분이 모든 경기를 90분씩 뛰었을 때의 몇 배인지 구합니다.

입력 이름: `s`

읽을 때 따라갈 호출(중복 제외): `min`



### `_age_fit` — 45행

기존 나이 규칙을 유지합니다. 26~30세는 0, 벗어난 만큼 음수입니다.

실제 경기력으로 검증한 최적 나이 기준이라는 뜻은 아닙니다.

입력 이름: `s`

읽을 때 따라갈 호출(중복 제외): `player_age`, `abs`, `max`



### `_cards_90` — 60행

입력 이름: `s`

읽을 때 따라갈 호출(중복 제외): `_p90`



### `_v` — 64행

가상 기록에서 특정 컬럼을 꺼내는 함수를 만듭니다.

예: _v('distance_km_90')는 해당 거리 값을 읽는 함수입니다.

입력 이름: `key`

읽을 때 따라갈 호출(중복 제외): `virtual_data.get`



### `label` — 479행

컬럼 키를 화면 이름으로 바꿉니다. 모르는 키는 그대로 돌려줍니다.

입력 이름: `key`



### `metric_keys` — 486행

한 포지션의 범주를 차례대로 돌며 컬럼 키를 모읍니다.

입력 이름: `pos`

읽을 때 따라갈 호출(중복 제외): `keys.append`



### `group_of` — 495행

컬럼이 어느 범주에 속하는지 찾아볼 사전을 만듭니다.

입력 이름: `pos`



### `default_group_weights` — 504행

예: 공격수의 {'finishing': 45.0, ...}를 만듭니다.

입력 이름: `pos`

읽을 때 따라갈 호출(중복 제외): `float`



### `group_weights` — 512행

범주 비율: 관리자 > 점수 기준에 저장한 값이 있으면 그것, 없으면 기본값.

입력 이름: `pos`

읽을 때 따라갈 호출(중복 제외): `default_group_weights`, `config.group_weights_for`



### `metric_weights` — 523행

범주 비중을 합계 100으로 맞추고, 각 컬럼에 똑같이 나눕니다.

입력 이름: `pos`, `groups`

읽을 때 따라갈 호출(중복 제외): `values.values`, `sum`, `group_weights`, `float`, `ValueError`, `groups.get`, `math.isfinite`, `len`



### `metric_values` — 551행

한 선수의 시즌 기록과 가상 기록으로 평가 항목 값을 만듭니다.

입력 이름: `stats`, `pos`

읽을 때 따라갈 호출(중복 제외): `for_player`, `metric_keys`, `calculate`



### `Normalizer` — 567행

정규화 도구: 같은 포지션에서 각 값의 위치를 0~1로 나타냅니다.

lo/hi/mean은 외부 코드에서도 쓰므로 이름을 유지합니다.
lo = 최저값, hi = 최고값, mean = 평균값입니다.

클래스 안의 작업: `__init__`, `fill`, `unit`

