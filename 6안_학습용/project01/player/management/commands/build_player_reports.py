# 공부 지도: learning/files/player/management/commands/build_player_reports.py.md
# 역할: 선수 기록·공통 점수·BEST11·연구실
"""선수별 분석 보고서(리그 전체)를 만들어 player/static/player/data/player_reports.json 에 저장한다.

사용: python manage.py build_player_reports
선수 기록(2026 시즌)을 새로 넣은 뒤 다시 실행하면 보고서가 갱신된다. DB 는 바꾸지 않는다(읽기만).
"""

import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from player.lab import reports


class Command(BaseCommand):
    help = '선수별 분석 보고서 JSON 만들기'

    # 이 관리 명령어의 실행 시작점: 옵션을 읽고 해당 작업을 수행
    def handle(self, *args, **options):
        data = reports.build_all()
        out = (
            Path(settings.BASE_DIR)
            / 'player'
            / 'static'
            / 'player'
            / 'data'
            / 'player_reports.json'
        )
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            json.dumps(data, ensure_ascii=False, separators=(',', ':')),
            encoding='utf-8',
        )
        self.stdout.write(
            self.style.SUCCESS(
                f"선수 {data['meta']['count']}명 보고서를 저장했습니다: {out}"
            )
        )
