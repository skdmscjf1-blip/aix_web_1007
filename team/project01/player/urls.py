from django.urls import path

from . import views
from .best11_reasons import best11_reasons


app_name = 'player'


urlpatterns = [
    # 선수 목록
    path(
        'plist/',
        views.plist,
        name='plist',
    ),

    # 선수 상세
    path(
        'pview/<int:id>/',
        views.pview,
        name='pview',
    ),

    # BEST11 경기장
    path(
        'best11/',
        views.best11,
        name='best11',
    ),

    # BEST11 선정 근거
    path(
        'reasons/',
        best11_reasons,
        name='best11_reasons',
    ),

    # 선수 팝업 정보
    path(
        'info/<int:id>/',
        views.player_info,
        name='player_info',
    ),
]