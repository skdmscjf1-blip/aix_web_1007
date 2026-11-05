# 공부 지도: learning/files/home/apps.py.md
# 역할: 메인 화면
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
