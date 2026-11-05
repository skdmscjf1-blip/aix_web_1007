# 공부 지도: learning/files/manager/admin.py.md
# 역할: 데이터 검토·업로드·백업·기준 관리
# Django 관리자에서 보일 목록·검색·필터를 정합니다.
from django.contrib import admin
from .models import (
    ImportBatch,
    StatColumn,
    ExtraStat,
    ScoreConfig,
    ScoreConfigLog,
    BestExclusion,
)

admin.site.register(ImportBatch)
admin.site.register(StatColumn)
admin.site.register(ExtraStat)
admin.site.register(ScoreConfig)
admin.site.register(ScoreConfigLog)
admin.site.register(BestExclusion)
