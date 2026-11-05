# 공부 지도: learning/files/player/lab/urls.py.md
# 역할: 선수 기록·공통 점수·BEST11·연구실
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.urls import path

from . import views

urlpatterns = [
    path('init/', views.lab_init, name='lab_init'),
    path('lineup/', views.lab_lineup, name='lab_lineup'),
    path('evaluate/', views.lab_evaluate, name='lab_evaluate'),
    path('candidates/', views.lab_candidates, name='lab_candidates'),
    path('condition/', views.lab_condition, name='lab_condition'),
    path('schedule/', views.lab_schedule, name='lab_schedule'),
    path('formations/', views.lab_formations, name='lab_formations'),
    path('player-report/', views.lab_player_report, name='lab_player_report'),
    path('chem-partners/', views.lab_chem_partners, name='lab_chem_partners'),
    path('quality/', views.lab_quality, name='lab_quality'),
]
