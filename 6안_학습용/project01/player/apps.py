# 공부 지도: learning/files/player/apps.py.md
# 역할: 선수 기록·공통 점수·BEST11·연구실
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class PlayerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'player'
