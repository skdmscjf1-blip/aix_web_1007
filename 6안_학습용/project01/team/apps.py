# 공부 지도: learning/files/team/apps.py.md
# 역할: 구단 기록·승무패 확률·라인업 실험
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class TeamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'team'
