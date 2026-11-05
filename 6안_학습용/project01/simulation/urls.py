# 공부 지도: learning/files/simulation/urls.py.md
# 역할: 가상 좌표 생성·GPS/이벤트 계산·경기별 저장
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.urls import path

from . import views

app_name = "simulation"

urlpatterns = [
    path(
        "<uuid:run_id>/replay/",
        views.replay,
        name="replay",
    ),
]
