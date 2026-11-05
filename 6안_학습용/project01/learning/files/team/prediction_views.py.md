# `team/prediction_views.py`

구단 기록·기본 승무패 예측·라인업 실험



[실제 코드 열기](../../../team/prediction_views.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from team.gps_prediction_features import build_gps_features

from team.player_prediction_features import build_player_features

from datetime import date, timedelta

from django import forms

from django.shortcuts import render

from django.utils import timezone

from team.match_prediction import PredictionUnavailable, forecast, load_bundle, load_matches, team_options

```

## 함수·클래스 안내

### `MatchPredictionForm` — 20행

클래스 안의 작업: `__init__`, `clean`



### `predict_match` — 85행

입력 이름: `request`

읽을 때 따라갈 호출(중복 제외): `render`, `load_matches`, `load_bundle`, `team_options`, `date.fromisoformat`, `MatchPredictionForm`, `context.update`, `max`, `form.is_valid`, `str`, `timezone.localdate`, `forecast`, `build_player_features`, `build_gps_features`, `timedelta`, `form.add_error`

