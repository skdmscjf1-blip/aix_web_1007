# `player/lab/club_profile.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../../player/lab/club_profile.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

```

## 함수·클래스 안내

### `_num` — 35행

입력 이름: `v`

읽을 때 따라갈 호출(중복 제외): `float`



### `team_metrics` — 42행

rows: [{'team_id', AGG_FIELDS...}] -> {team_id: {지표...}}  (경기당 = 총 출전시간 / 990)

입력 이름: `rows`

읽을 때 따라갈 호출(중복 제외): `sums.items`, `r.get`, `sums.setdefault`, `_num`



### `_z` — 71행

입력 이름: `values`

읽을 때 따라갈 호출(중복 제외): `len`, `sum`



### `classify` — 88행

metrics: team_metrics 결과 -> {team_id: {'style','label','scores':{스타일:점수},'metrics'}}

입력 이름: `metrics`, `threshold`

읽을 때 따라갈 호출(중복 제외): `list`, `len`, `dict`, `STYLE_FORMULA.items`, `max`, `zip`, `round`, `_z`, `sum`, `metrics[t].items`

