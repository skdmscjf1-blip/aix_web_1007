# `player/models.py`

선수 조회·공통 평가·BEST11·연구실 — 저장 항목과 테이블 관계



[실제 코드 열기](../../../player/models.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from django.db import models

from team.models import Team

```

## 함수·클래스 안내

### `Player` — 11행

DB 필드:

- `team`: `models.ForeignKey`

- `name`: `models.CharField`

- `number`: `models.IntegerField`

- `position`: `models.CharField`

- `age`: `models.IntegerField`

- `height`: `models.IntegerField`

- `weight`: `models.IntegerField`

- `birth_date`: `models.DateField`

- `photo`: `models.ImageField`

클래스 안의 작업: `__str__`



### `PlayerStats` — 48행

DB 필드:

- `player`: `models.ForeignKey`

- `season`: `models.IntegerField`

- `minutes`: `models.IntegerField`

- `goals`: `models.IntegerField`

- `assists`: `models.IntegerField`

- `games`: `models.IntegerField`

- `attack_points`: `models.IntegerField`

- `pk_goals`: `models.IntegerField`

- `mom`: `models.IntegerField`

- `average_rating`: `models.FloatField`

- `best11_count`: `models.IntegerField`

- `pk_attempts`: `models.IntegerField`

- `shots`: `models.IntegerField`

- `shots_on_target`: `models.IntegerField`

- `shots_blocked`: `models.IntegerField`

- `shots_off_target`: `models.IntegerField`

- `shots_inside_box`: `models.IntegerField`

- `shots_outside_box`: `models.IntegerField`

- `offsides`: `models.IntegerField`

- `free_kicks`: `models.IntegerField`

- `corner_kicks`: `models.IntegerField`

- `throw_ins`: `models.IntegerField`

- `dribble_attempt`: `models.IntegerField`

- `dribble_success`: `models.IntegerField`

- `pass_attempt`: `models.IntegerField`

- `pass_success`: `models.IntegerField`

- `key_passes`: `models.IntegerField`

- `forward_pass_attempt`: `models.IntegerField`

- `forward_pass_success`: `models.IntegerField`

- `backward_pass_attempt`: `models.IntegerField`

- `backward_pass_success`: `models.IntegerField`

- `lateral_pass_attempt`: `models.IntegerField`

- `lateral_pass_success`: `models.IntegerField`

- `attacking_third_pass_attempt`: `models.IntegerField`

- `attacking_third_pass_success`: `models.IntegerField`

- `defensive_third_pass_attempt`: `models.IntegerField`

- `defensive_third_pass_success`: `models.IntegerField`

- `middle_third_pass_attempt`: `models.IntegerField`

- `middle_third_pass_success`: `models.IntegerField`

- `long_pass_attempt`: `models.IntegerField`

- `long_pass_success`: `models.IntegerField`

- `medium_pass_attempt`: `models.IntegerField`

- `medium_pass_success`: `models.IntegerField`

- `short_pass_attempt`: `models.IntegerField`

- `short_pass_success`: `models.IntegerField`

- `cross_attempt`: `models.IntegerField`

- `cross_success`: `models.IntegerField`

- `escape_pressure`: `models.IntegerField`

- `ground_duel_attempt`: `models.IntegerField`

- `ground_duel_success`: `models.IntegerField`

- `aerial_duel_attempt`: `models.IntegerField`

- `aerial_duel_success`: `models.IntegerField`

- `tackle_attempt`: `models.IntegerField`

- `tackle_success`: `models.IntegerField`

- `clearances`: `models.IntegerField`

- `interceptions`: `models.IntegerField`

- `defensive_blocks`: `models.IntegerField`

- `recoveries`: `models.IntegerField`

- `blocks`: `models.IntegerField`

- `ball_misses`: `models.IntegerField`

- `fouls`: `models.IntegerField`

- `fouls_won`: `models.IntegerField`

- `yellow_cards`: `models.IntegerField`

- `red_cards`: `models.IntegerField`

클래스 안의 작업: `pass_success_rate`, `dribble_success_rate`, `cross_success_rate`, `ground_duel_success_rate`, `aerial_duel_success_rate`, `tackle_success_rate`, `per90`, `goals_per90`, `assists_per90`, `shots_per90`, `shots_on_target_per90`, `key_passes_per90`, `dribble_success_per90`, `interceptions_per90`, `clearances_per90`, `recoveries_per90`, `tackle_success_per90`, `__str__`

