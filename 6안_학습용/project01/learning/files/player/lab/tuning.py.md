# `player/lab/tuning.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../../player/lab/tuning.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

```

## 함수·클래스 안내

### `_is_top` — 49행

입력 이름: `team`, `table`, `key`

읽을 때 따라갈 호출(중복 제외): `sorted`, `max`, `round`, `table.values`, `len`, `sum`



### `opponent_multipliers` — 57행

opp: 상대 구단 id, club: club_profile.classify 결과, goals: {구단 id: {'gf','ga'}} (경기당, 없으면 생략)
반환: (지표별 배율 dict, 이유 문장 리스트)

입력 이름: `opp`, `club`, `goals`

읽을 때 따라갈 호출(중복 제외): `club.get`, `rule[0].items`, `reasons.append`, `apply`, `_is_top`, `round`, `max`, `mult.get`, `min`

