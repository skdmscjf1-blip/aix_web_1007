# 공부 지도: learning/files/soccer_game/urls.py.md
# 역할: 축구게임 진입과 브라우저 리소스
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.urls import path
from . import views

app_name = 'soccer_game'

urlpatterns = [
    path('game/', views.game, name='game'),
]
