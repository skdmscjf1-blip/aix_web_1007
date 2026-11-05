# `player/lab/management.py`

가상 경기의 피로·경고·일정 관련 규칙



[실제 코드 열기](../../../../player/lab/management.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

import json

import math

from datetime import date, datetime

```

## 함수·클래스 안내

### `_num` — 62행

입력 이름: `v`

읽을 때 따라갈 호출(중복 제외): `float`



### `age_on` — 69행

birth_date: 'YYYY-MM-DD' 또는 date. on: date. 모르면 None.

입력 이름: `birth_date`, `on`

읽을 때 따라갈 호출(중복 제외): `isinstance`, `datetime.strptime(str(birth_date)[:10], '%Y-%m-%d').date`, `datetime.strptime`, `str`



### `load_schedule` — 89행

공식 경기 JSON(official_source_*.json)에서 정규 리그 일정을 읽는다.
반환: {'rounds': {라운드: {'date','played'}}, 'team_dates': {팀명: [(라운드, date)]}, 'fixtures': {팀명: [{'round','date','opponent','home','played'}]}}
주의: 'played' 는 파일을 받은 시점 기준이다 (endYn). 파일이 오래되면 실제와 다를 수 있다.

입력 이름: `path`, `league_id`

찾아볼 반환 사전 키(분기·내부 함수 포함): `rounds`, `team_dates`, `fixtures`

읽을 때 따라갈 호출(중복 제외): `d['months'].values`, `open`, `json.load`, `datetime.strptime(g['gameDate'], '%Y.%m.%d').date`, `rounds.setdefault`, `min`, `team_dates[t].sort`, `fixtures[t].sort`, `isinstance`, `data.get`, `team_dates.setdefault(t, []).append`, `fixtures.setdefault(t, []).append`, `g.get`, `datetime.strptime`, `team_dates.setdefault`, `fixtures.setdefault`



### `first_unplayed_round` — 130행

시작 라운드: 아직 열리지 않은 첫 라운드.
파일의 'played' 표시와 오늘 날짜를 둘 다 본다. (파일이 오래돼서 이미 치른 라운드가 '미종료'로 남아 있을 수 있어서)

입력 이름: `schedule`, `today`

읽을 때 따라갈 호출(중복 제외): `sorted`, `date.today`



### `days_between_rounds` — 143행

팀 기준으로 두 라운드 경기 사이의 일수.

입력 이름: `schedule`, `team`, `round_a`, `round_b`

읽을 때 따라갈 호출(중복 제외): `dict`, `schedule['team_dates'].get`, `schedule['rounds'].get`



### `baseline_fatigue` — 159행

시즌 평균 출전시간으로 구한 시작 피로도. 항상 풀타임이면 BASELINE_MAX.

입력 이름: `minutes`, `games`

읽을 때 따라갈 호출(중복 제외): `_num`, `round`, `min`



### `streak_cost` — 168행

streak: 이번 경기까지 포함한 연속 출전 횟수(1 = 직전 라운드를 쉬었음).

입력 이름: `streak`

읽을 때 따라갈 호출(중복 제외): `max`, `min`, `int`, `len`



### `match_fatigue` — 174행

한 경기로 쌓이는 피로도. 출전 시간에 비례하고, 연속 출전 횟수에 따라 풀타임 기준값이 커진다.

입력 이름: `minutes_played`, `position`, `streak`

읽을 때 따라갈 호출(중복 제외): `min`, `max`, `streak_cost`, `(position or '').upper`, `_num`



### `recovery` — 187행

입력 이름: `days`, `age`

읽을 때 따라갈 호출(중복 제외): `max`



### `fatigue_tier` — 194행

입력 이름: `fatigue`

찾아볼 반환 사전 키(분기·내부 함수 포함): `multiplier`, `label`



### `adjusted_ability` — 201행

피로도를 반영한 능력 점수.

입력 이름: `ability`, `fatigue`

읽을 때 따라갈 호출(중복 제외): `fatigue_tier`



### `card_probability` — 211행

다음 경기에서 경고를 받을 확률(%): 시즌 경고 비율(90분당)을 이 경기 출전 시간으로 환산해 포아송으로 계산.
선수 개인의 '성향'이 아니라 올 시즌 기록의 단순 환산이다.

입력 이름: `season_yellow`, `season_red`, `season_minutes`, `minutes_this_match`

읽을 때 따라갈 호출(중복 제외): `_num`, `round`, `max`, `math.exp`



### `card_risk_label` — 223행

입력 이름: `probability`



### `caution_multiplier` — 231행

누적 경고가 많을수록 신중하게 뛰어 능력이 소폭 낮아지는 효과 (게임 규칙).

입력 이름: `yellow_acc`

읽을 때 따라갈 호출(중복 제외): `_num`



### `adjusted_ability` — 240행

피로도와 신중 플레이 효과를 모두 반영한 능력 점수.

입력 이름: `ability`, `fatigue`, `yellow_acc`

읽을 때 따라갈 호출(중복 제외): `caution_multiplier`, `fatigue_tier`



### `availability` — 247행

배지 목록. 정지 규칙이 없으므로 항상 기용 가능하다.

입력 이름: `player_state`, `risk_percent`

찾아볼 반환 사전 키(분기·내부 함수 포함): `available`, `badges`, `multiplier`

읽을 때 따라갈 호출(중복 제외): `fatigue_tier`, `card_risk_label`, `player_state.get`, `badges.append`, `caution_multiplier`



### `initial_state` — 271행

players: [{'id','position','birth_date','minutes','games','yellow_cards'}]
반환: {player_id(str): {'fatigue','yellow_acc','streak'}}
누적 경고(yellow_acc)의 시작값은 올 시즌 실제 경고 수다.

입력 이름: `players`, `today`

읽을 때 따라갈 호출(중복 제외): `str`, `baseline_fatigue`, `int`, `p.get`, `_num`



### `pre_match_fatigue` — 287행

다음 경기 직전의 피로도 (직전 경기 후 휴식일만큼 회복한 값).

입력 이름: `st`, `days`, `age`

읽을 때 따라갈 호출(중복 제외): `max`, `st.get`, `recovery`



### `advance_round` — 292행

라운드 하나를 진행한다. (state 를 바꾸지 않고 새로 만들어 돌려준다)
played: {player_id: 출전 분}   meta: {player_id: {'position','age','season_yellow','season_red','season_minutes'}}
days_since_last: {player_id: 지난 경기 이후 일수}(없으면 7)
rng: random.Random — 있으면 경고 발생을 추첨하고, None 이면 추첨하지 않는다.
반환: (새 상태, 이벤트 리스트)

입력 이름: `state`, `played`, `meta`, `days_since_last`, `rng`

읽을 때 따라갈 호출(중복 제외): `state.items`, `dict`, `meta.get`, `played.get`, `pre_match_fatigue`, `days_since_last.get`, `m.get`, `min`, `st.get`, `match_fatigue`, `card_probability`, `rng.random`, `events.append`, `max`

