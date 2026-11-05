# 공부 지도: learning/files/board/apps.py.md
# 역할: 회원·게시글·댓글·신고 관리
# Django에 앱을 등록하고 시작할 때 필요한 작업을 연결합니다.
from django.apps import AppConfig


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'
    verbose_name = '자유게시판'

    def ready(self):
        from . import signals  # noqa: F401  (금칙어를 추가하면 기존 글도 자동 검사)
