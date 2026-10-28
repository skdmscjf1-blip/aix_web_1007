from django.shortcuts import render

from player.services import get_filtered_best11, get_formations
from team.models import Team


METRIC_LABELS = {
    'goals': '득점 / 90분',
    'assists': '도움 / 90분',
    'shots_on_target': '유효슈팅 / 90분',
    'shots': '슈팅 / 90분',
    'key_passes': '키패스 / 90분',
    'dribble': '드리블 성공 / 90분',
    'pass_rate': '패스 성공률 (%)',
    'recoveries': '볼 회수 / 90분',
    'interceptions': '인터셉트 / 90분',
    'clearances': '클리어링 / 90분',
    'tackle': '태클 성공 / 90분',
    'aerial_duel': '공중 경합 성공 / 90분',
    'ground_duel': '지상 경합 성공 / 90분',
    'defensive_blocks': '수비 차단 / 90분',
    'blocks': '블록 / 90분',
    'conceding': '실점 억제 지표 (0~1)',
    'clean_sheet_rate': '무실점 경기 비율 (%)',
    'rating': '평균평점',
    'mom': 'MOM 선정 / 90분',
    'best11': 'BEST11 선정 / 90분',
    'minutes': '출전시간 (분)',
}


def best11_reasons(request):
    result = get_filtered_best11(
        team_id=request.GET.get('team', ''),
        formation=request.GET.get('formation', '4-3-3'),
    )

    players = []

    for position, rows in result['best11'].items():
        for row in rows:
            metrics = [
                {
                    'label': METRIC_LABELS.get(key, key),
                    'value': value,
                    'normalized': row['normalized'][key],
                    'points': row['contributions'][key],
                }
                for key, value in row['metrics'].items()
            ]

            metrics.sort(
                key=lambda item: item['points'],
                reverse=True,
            )

            players.append({
                'player': row['player'],
                'position': position,
                'minutes': row['stats'].minutes,
                'score': row['score'],
                'official_eligible': row['stats'].minutes >= 600,
                'metrics': metrics,
                'strengths': [
                    item for item in metrics
                    if item['points'] > 0
                ][:3],
                'legacy_gk': (
                    position == 'GK'
                    and 'conceding' not in row['metrics']
                ),
            })

    return render(
        request,
        'player/best11_reasons.html',
        {
            'result': result,
            'players': players,
            'teams': Team.objects.order_by('team_name'),
            'formations': get_formations(),
        },
    )