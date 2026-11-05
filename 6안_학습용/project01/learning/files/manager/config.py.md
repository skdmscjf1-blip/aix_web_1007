# `manager/config.py`

저장된 관리자 비중을 읽고 필요하면 코드 기본값으로 대체



[실제 코드 열기](../../../manager/config.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import contextlib

import threading

```

## 함수·클래스 안내

### `load_saved` — 52행

DB에 저장된 설정 (없으면 빈 dict)

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `ScoreConfig.objects.first`, `dict`



### `_data` — 60행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `getattr`, `load_saved`



### `override` — 66행

저장하지 않고 이 안에서만 다른 설정으로 계산해 본다 (미리보기용)

입력 이름: `data`

읽을 때 따라갈 호출(중복 제외): `getattr`



### `min_minutes` — 76행

입력 이름: `default_best11`, `default_formation`

찾아볼 반환 사전 키(분기·내부 함수 포함): `best11`, `formation`

읽을 때 따라갈 호출(중복 제외): `_data().get`, `int`, `_data`, `d.get`



### `player_weight` — 84행

승부예측에서 '선수 능력치' 부분의 비중(%). 나머지는 팀 기록(최근 5경기·홈/원정·시즌). 0~60.

입력 이름: `default`

읽을 때 따라갈 호출(중복 제외): `max`, `float`, `min`, `_data().get`, `_data`



### `group_weights_for` — 93행

통합 선수 점수의 범주 비율 (BEST11 · 감독 연구실 · 승부예측 공통). 저장값이 없으면 기본값.

입력 이름: `position`, `default`

읽을 때 따라갈 호출(중복 제외): `_data().get('groups', {}).get`, `dict`, `_data().get`, `max`, `sum`, `float`, `out.values`, `_data`, `g.get`



### `weights_for` — 107행

입력 이름: `position`, `default`

읽을 때 따라갈 호출(중복 제외): `_data().get('weights', {}).get`, `float`, `_data().get`, `w.get`, `_data`



### `exclusions_initialized` — 114행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `bool`, `_data().get`, `_data`



### `excluded_ids` — 118행

입력 이름: `default_ids`

읽을 때 따라갈 호출(중복 제외): `_data`, `d.get`, `list`, `BestExclusion.objects.values_list`

