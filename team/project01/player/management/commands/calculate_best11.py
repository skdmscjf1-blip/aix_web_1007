from django.core.management.base import BaseCommand

from player.services import get_best11


class Command(BaseCommand):
    help = '웹 화면과 같은 공통 평가 함수로 2026 공식 BEST11과 TOP10을 출력합니다.'

    def handle(self, *args, **options):
        result = get_best11()
        self.stdout.write('2026 K리그 공식 BEST11 (600분 이상, 점수 비교군 450분 이상)')
        self.stdout.write(f"전체 후보: {result['candidate_count']}명")
        for position, rows in result['rankings'].items():
            self.stdout.write(f'\n{position} TOP10')
            for rank, row in enumerate(rows[:10], start=1):
                player = row['player']
                self.stdout.write(
                    f"{rank}위 / {player.name} / {player.team.team_name} / {row['score']:.2f}점"
                )
        self.stdout.write('\n4-3-3 공식 BEST11')
        for position, rows in result['best11'].items():
            self.stdout.write(position + ': ' + ', '.join(row['player'].name for row in rows))
        self.stdout.write('DB를 수정하지 않았습니다. GK 평가 기준은 웹 화면 안내를 확인하세요.')
