# 공부 지도: learning/files/board/management/commands/scan_board.py.md
# 역할: 회원·게시글·댓글·신고 관리
from django.core.management.base import BaseCommand

from board.filters import scan_all


class Command(BaseCommand):
    help = '이미 올라온 게시글·댓글에서 금칙어를 찾아 자동으로 숨김 처리합니다.'

    # 이 관리 명령어의 실행 시작점: 옵션을 읽고 해당 작업을 수행
    def handle(self, *args, **opts):
        p, c = scan_all()
        self.stdout.write(f'글 {p}개, 댓글 {c}개를 숨김 처리했습니다.')
