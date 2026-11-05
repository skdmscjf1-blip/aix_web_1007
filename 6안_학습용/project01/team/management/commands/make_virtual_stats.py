# 공부 지도: learning/files/team/management/commands/make_virtual_stats.py.md
# 역할: 구단 기록·승무패 확률·라인업 실험
from django.core.management.base import BaseCommand

from team import virtual_stats


class Command(BaseCommand):
    help = '승부예측용 가상 데이터(골키퍼 선방·실점, 활동량 등)를 data/virtual/2026_virtual_stats.json 에 만듭니다. 실제 기록이 아닙니다.'

    # 이 관리 명령어의 실행 시작점: 옵션을 읽고 해당 작업을 수행
    def handle(self, *args, **options):
        p, data = virtual_stats.save()
        gk = sum(1 for v in data['players'].values() if 'save_rate' in v)
        self.stdout.write(
            self.style.SUCCESS(
                f"가상 데이터 {len(data['players'])}명(골키퍼 {gk}명)을 저장했습니다: {p}"
            )
        )
        self.stdout.write(virtual_stats.NOTE)
