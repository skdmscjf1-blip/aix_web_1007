# 공부 지도: learning/files/soccer_game/views.py.md
# 역할: 축구게임 진입과 브라우저 리소스
# 요청에서 조건을 읽고 계산 결과를 HTML 또는 JSON으로 돌려줍니다.
from django.shortcuts import render


# 축구게임 템플릿 후보를 기존 순서대로 찾아 화면을 표시
def game(request):
    return render(
        request,
        [
            'soccer_game.html',
            'soccer_game/pending.html',
        ],
    )
