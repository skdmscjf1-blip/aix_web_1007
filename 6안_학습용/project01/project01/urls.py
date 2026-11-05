# 공부 지도: learning/files/project01/urls.py.md
# 역할: Django 실행 설정과 전체 주소 연결
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(
        '',
        include('home.urls'),
    ),
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        'player/',
        include('player.urls'),
    ),
    path(
        'team/',
        include('team.urls'),
    ),
    path(
        'board/',
        include('board.urls'),
    ),
    path(
        'manager/',
        include('manager.urls'),
    ),
    path(
        'soccer_game/',
        include('soccer_game.urls'),
    ),
    path("simulation/", include("simulation.urls")),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
