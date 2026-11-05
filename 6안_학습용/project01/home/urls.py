# 공부 지도: learning/files/home/urls.py.md
# 역할: 메인 화면
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.

from django.urls import path, include
from . import views

app_name = ''

urlpatterns = [
    path('', views.index, name='index'),
]
