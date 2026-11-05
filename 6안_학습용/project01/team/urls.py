# 공부 지도: learning/files/team/urls.py.md
# 역할: 구단 기록·승무패 확률·라인업 실험
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.urls import path

from .prediction_views import predict_match

from .simulation_views import (
    simulation_page,
    simulation_roster,
    simulation_result,
)


app_name = 'team'


urlpatterns = [
    # 기본 승무패 예측 화면
    path(
        'predict/',
        predict_match,
        name='predict_match',
    ),
    # 선수 교체·컨디션 시뮬레이션 화면
    path(
        'simulate/',
        simulation_page,
        name='simulate',
    ),
    # 선택한 구단의 선수 명단
    path(
        'simulation/roster/',
        simulation_roster,
        name='simulation_roster',
    ),
    # 사용자 설정에 따른 시뮬레이션 계산
    path(
        'simulation/result/',
        simulation_result,
        name='simulation_result',
    ),
]
