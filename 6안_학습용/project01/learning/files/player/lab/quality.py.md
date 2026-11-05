# `player/lab/quality.py`

선수 조회·공통 평가·BEST11·연구실



[실제 코드 열기](../../../../player/lab/quality.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

```

## 함수·클래스 안내

### `_n` — 69행

입력 이름: `v`

읽을 때 따라갈 호출(중복 제외): `float`



### `_median` — 76행

입력 이름: `xs`

읽을 때 따라갈 호출(중복 제외): `sorted`, `len`



### `check` — 84행

rows: [{'id','name','team_id','team','position','birth_date','minutes','games', ...기록 필드...}]
반환: {'summary': {'error':n,'warn':n,'info':n,'players':N}, 'issues': [{'severity','code','title','count','examples':[...]}]}

입력 이름: `rows`, `team_min`, `team_max`

찾아볼 반환 사전 키(분기·내부 함수 포함): `summary`, `issues`

읽을 때 따라갈 호출(중복 제외): `seen.items`, `per_team.items`, `by_pos.items`, `sorted`, `buckets.setdefault`, `(r.get('position') or '').strip().upper`, `seen.setdefault(key, []).append`, `per_team.setdefault(r.get('team') or '(소속 없음)', []).append`, `buckets.values`, `len`, `b['examples'].append`, `_n`, `add`, `r.get`, `(r.get('name') or '').strip`, `by_pos.setdefault((r.get('position') or '').strip().upper(), []).append`, `_median`, `max`, `zip`, `(r.get('position') or '').strip`, `repr`, `seen.setdefault`, `per_team.setdefault`, `sum`, `row.get`, `by_pos.setdefault`, `abs`, `int`

