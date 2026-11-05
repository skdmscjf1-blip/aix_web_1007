# 공부 지도: learning/files/manager/urls.py.md
# 역할: 데이터 검토·업로드·백업·기준 관리
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('import/', views.import_upload, name='import_upload'),
    path('import/<int:pk>/', views.import_report, name='import_report'),
    path('import/<int:pk>/apply/', views.import_apply, name='import_apply'),
    path('history/', views.history, name='history'),
    path('scoring/', views.scoring, name='scoring'),
    path('exclusions/', views.exclusions, name='exclusions'),
    path('backups/', views.backups, name='backups'),
    path('backups/now/', views.backup_now, name='backup_now'),
    path('backups/<str:name>/restore/', views.backup_restore, name='backup_restore'),
]
