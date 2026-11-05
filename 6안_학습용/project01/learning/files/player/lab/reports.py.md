# `player/lab/reports.py`

근거 수치와 포지션 비교를 선수 보고서로 변환



[실제 코드 열기](../../../../player/lab/reports.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from datetime import date

from . import chemistry as CH

from . import service as SVC

```

## 함수·클래스 안내

### `_verdict` — 19행

입력 이름: `pct`, `minutes`



### `build_one` — 31행

입력 이름: `c`, `pid`, `peers_by_pos`, `teammates_by_key`

찾아볼 반환 사전 키(분기·내부 함수 포함): `id`, `name`, `team`, `position`, `verdict`, `conclusion`, `rule`, `basis`, `confidence`, `ability`, `rank`, `rank_total`, `top_pct`, `ranked`, `team_rank`, `team_rank_total`, `club_style`, `rows`, `why`, `hire`, `cautions`, `partners`, `similar`

읽을 때 따라갈 호출(중복 제외): `c.ability.get`, `SVC._breakdown`, `max`, `sorted`, `SVC.MG.card_probability`, `SVC.MG.card_risk_label`, `c.data['club'].get`, `_verdict`, `SVC._evidence(r).replace`, `sum`, `round`, `any`, `getattr`, `why.append`, `', '.join`, `hire.append`, `cautions.append`, `len`, `str`, `teammates_by_key.get`, `mates_sorted.index`, `c.profiles.values`, `CH.recommend_partners`, `SVC._evidence`, `next`, `ev`, `SVC.J`, `'; '.join`



### `per90_scale` — 253행

선수 팝업 '90분당 주요 기록' 가로바용 기준. 포지션별 주전급(450분 이상) 평균·최대. pass_rate 는 성공률(%).

입력 이름: `c`

읽을 때 따라갈 호출(중복 제외): `PER90_KEYS.items`, `c.data['stats'].items`, `round`, `max`, `st.player.position.strip().upper`, `sum`, `len`, `getattr`, `st.player.position.strip`



### `build_all` — 285행

리그 전체 선수의 보고서. 기본 설정(가중치 기본, 케미 1×, 경험 보정 기본값).

입력 이름: 

찾아볼 반환 사전 키(분기·내부 함수 포함): `meta`, `players`

읽을 때 따라갈 호출(중복 제외): `SVC.Ctx`, `c.profiles.values`, `sorted`, `tm.setdefault((q['team_id'], q['position']), []).append`, `build_one`, `per90_scale`, `date.today().isoformat`, `len`, `tm.setdefault`, `str`, `date.today`

