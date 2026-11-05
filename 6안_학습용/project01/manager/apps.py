# 공부 지도: learning/files/manager/apps.py.md
# 역할: 데이터 검토·업로드·백업·기준 관리
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class ManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager'
