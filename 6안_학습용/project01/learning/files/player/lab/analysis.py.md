# `player/lab/analysis.py`

선수 대체·기여도와 명단 분석



[실제 코드 열기](../../../../player/lab/analysis.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

```

## 함수·클래스 안내

### `short_name` — 51행

입력 이름: `team_name`

읽을 때 따라갈 호출(중복 제외): `FULL_TO_SHORT.get`



### `lineup_total` — 60행

라인업의 총점 = 각 선수의 (피로·경고 반영 능력 점수) + 케미 가산점.
반환: (총점, lineup_chemistry 결과)

입력 이름: `lineup`, `ability`, `state`, `chem_scale`

읽을 때 따라갈 호출(중복 제외): `CH.lineup_chemistry`, `state.get`, `ability.get`, `MG.adjusted_ability`, `CH.final_score`, `str`, `st.get`



### `lineup_strength_factor` — 80행

라인업 평균 능력이 기준보다 높으면 1보다 큰 배율(상한 ±LINEUP_EFFECT_CAP).

입력 이름: `lineup_mean`, `reference_mean`

읽을 때 따라갈 호출(중복 제외): `max`, `min`



### `opponent_outlook` — 86행

team 의 남은 대진과 예상 결과.
forecast_fn(home_short, away_short, date) -> 팀 예측 모델의 forecast 결과(dict). 예측 불가면 예외.
factor != 1 이고 poisson_fn 이 있으면 내 예상 득점에 factor 를 곱해 확률을 다시 계산한다(라인업 보정).

입력 이름: `fixtures`, `team`, `forecast_fn`, `from_round`, `count`, `factor`, `poisson_fn`

읽을 때 따라갈 호출(중복 제외): `fixtures.get`, `row.update`, `out.append`, `len`, `f['date'].isoformat`, `forecast_fn`, `str`, `abs`, `poisson_fn`, `round`



### `plan_rotation` — 154행

남은 라운드(rounds) 동안 같은 라인업을 쓰되, 피로가 많이 쌓일 선수는 같은 포지션 후보와 교체하는 계획.
lineup/bench: 프로필 리스트, state/meta: management 의 상태와 선수 정보,
meta[pid] = {'position','age','team'(짧은 이름),'season_yellow','season_red','season_minutes'}
반환: {'rounds':[...], 'peak_without_rotation':, 'peak_with_rotation':}

입력 이름: `lineup`, `bench`, `state`, `meta`, `rounds`, `ability`, `prev_round`, `schedule`, `rest_limit`

찾아볼 반환 사전 키(분기·내부 함수 포함): `rounds`, `peak_with_rotation`, `peak_without_rotation`

읽을 때 따라갈 호출(중복 제외): `simulate`, `MG.days_between_rounds`, `round`, `meta[str(pid)].get`, `dict`, `MG.advance_round`, `max`, `plan.append`, `state.items`, `days`, `risky.sort`, `str`, `MG.pre_match_fatigue`, `list`, `st[str(pid)].get`, `MG.match_fatigue`, `risky.append`, `MG.adjusted_ability`, `swaps.append`, `ability.get`, `st[str(b['id'])].get`, `cur.index`, `sum`, `len`



### `irreplaceability` — 265행

각 선수를 같은 포지션의 최선 대체 후보로 바꿨을 때 라인업 총점이 얼마나 떨어지는가.
지수 = 총점 하락폭(≥0). index100 은 라인업 내 최대 하락폭을 100 으로 환산한 값.

입력 이름: `lineup`, `pool`, `ability`, `state`, `chem_scale`

찾아볼 반환 사전 키(분기·내부 함수 포함): `total`, `players`

읽을 때 따라갈 호출(중복 제외): `lineup_total`, `enumerate`, `sorted`, `cands.sort`, `results.append`, `max`, `round`, `list`, `ability.get`



### `_percentile_of` — 323행

입력 이름: `value`, `sorted_vals`

읽을 때 따라갈 호출(중복 제외): `len`, `sum`



### `lineup_report` — 330행

reference_abilities: {포지션: [리그 기준 선수들의 능력 점수]}  (라인별 위치 계산용)
chem: lineup_chemistry 결과, irr: irreplaceability 결과

입력 이름: `lineup`, `ability`, `state`, `meta`, `chem`, `irr`, `reference_abilities`, `today`

읽을 때 따라갈 호출(중복 제외): `sorted`, `max`, `min`, `notes.append`, `report['lines'].append`, `p['cats'].items`, `round`, `cats.items`, `team_count.items`, `meta[str(p['id'])].get`, `state.get(str(p['id']), {}).get`, `sum`, `meta[str(next((p['id'] for p in lineup if p['team_id'] == top_team_id)))].get`, `len`, `reference_abilities.items`, `team_count.get`, `sums.get`, `cnt.get`, `meta.get(str(p['id']), {}).get`, `state.get`, `MG.card_probability`, `', '.join`, `_percentile_of`, `str`, `ability.get`, `refs.get`, `meta.get`, `next`

