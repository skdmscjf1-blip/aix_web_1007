# 공부 지도: learning/files/board/urls.py.md
# 역할: 회원·게시글·댓글·신고 관리
# 주소를 처리 함수에 연결합니다. 실제 입력·계산은 연결된 함수를 따라갑니다.
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import reverse_lazy

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('login/', views.BoardLogin.as_view(), name='login'),
    path(
        'logout/',
        LogoutView.as_view(next_page=reverse_lazy('board:login')),
        name='logout',
    ),
    path('signup/', views.signup, name='signup'),
    path('write/', views.post_create, name='create'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('<int:pk>/edit/', views.post_edit, name='edit'),
    path('<int:pk>/delete/', views.post_delete, name='delete'),
    path('<int:pk>/report/', views.post_report, name='report'),
    path('<int:pk>/comment/', views.comment_create, name='comment'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<int:pk>/report/', views.comment_report, name='comment_report'),
]
