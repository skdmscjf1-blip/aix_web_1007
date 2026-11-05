# 공부 지도: learning/files/simulation/apps.py.md
# 역할: 가상 좌표 생성·GPS/이벤트 계산·경기별 저장
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class SimulationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'simulation'
