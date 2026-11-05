# 공부 지도: learning/files/soccer_game/apps.py.md
# 역할: 축구게임 진입과 브라우저 리소스
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class SoccerGameConfig(AppConfig):
    name = 'soccer_game'
