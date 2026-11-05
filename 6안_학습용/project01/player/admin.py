# 공부 지도: learning/files/player/admin.py.md
# 역할: 선수 기록·공통 점수·BEST11·연구실
# Django 관리자에서 보일 목록·검색·필터를 정합니다.
from django.contrib import admin
from player.models import Player, PlayerStats

admin.site.register(Player)
admin.site.register(PlayerStats)
# Register your models here.
