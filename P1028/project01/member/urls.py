from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('step01/', views.step01, name='step01'),
    # 이메일전송
    path('emailsend/', views.emailsend, name='emailsend'),
    # 이메일전송 후 키 인증
    path('ekey/', views.ekey, name='ekey'),
]
