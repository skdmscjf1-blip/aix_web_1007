from django.shortcuts import render
from player.models import Player, PlayerStats
from team.models import Team
from player.services import get_best11


# =========================================================
# 선수 목록
# =========================================================
def plist(request):

    # GET 방식으로 검색조건 가져오기
    team_id = request.GET.get('team', '')
    position = request.GET.get('position', '')
    search_word = request.GET.get('search_word', '')

    # 전체 선수 가져오기
    qs = Player.objects.all()

    # -----------------------------------------------------
    # 구단 검색
    # -----------------------------------------------------
    if team_id:
        qs = qs.filter(team_id=team_id)

    # -----------------------------------------------------
    # 포지션 검색
    # -----------------------------------------------------
    if position:
        qs = qs.filter(position=position)

    # -----------------------------------------------------
    # 선수명 검색
    # -----------------------------------------------------
    if search_word:
        qs = qs.filter(name__contains=search_word)

    # -----------------------------------------------------
    # 정렬
    # 구단명 → 포지션 → 등번호 순
    # -----------------------------------------------------
    qs = qs.order_by(
        'team__team_name',
        'position',
        'number'
    )

    # 전체 구단 목록
    # 검색 select 박스에서 사용
    teams = Team.objects.all().order_by(
        'team_name'
    )

    # HTML로 전달할 데이터
    context = {
        'list': qs,
        'teams': teams,
        'team_id': team_id,
        'position': position,
        'search_word': search_word,
    }

    return render(
        request,
        'plist.html',
        context
    )


# =========================================================
# 선수 상세정보
# =========================================================
def pview(request, id):

    # -----------------------------------------------------
    # 선택한 선수 1명 가져오기
    #
    # URL 예:
    # /player/pview/10/
    #
    # id=10인 선수를 가져옴
    # -----------------------------------------------------
    qs = Player.objects.get(
        id=id
    )

    # -----------------------------------------------------
    # 해당 선수의 시즌별 성적 가져오기
    #
    # 최신 시즌부터 정렬
    # -----------------------------------------------------
    stats = PlayerStats.objects.filter(
        player=qs
    ).order_by(
        '-season'
    )

    # HTML로 전달
    context = {
        'player': qs,
        'stats': stats,
    }

    return render(
        request,
        'pview.html',
        context
    )


# =========================================================
# 2026 K리그 BEST11
# =========================================================
def best11(request):

    # -----------------------------------------------------
    # services.py에 만들어둔
    # BEST11 계산 함수를 실행
    #
    # views.py에서 직접 점수를 계산하지 않고
    # 계산은 services.py가 담당
    # -----------------------------------------------------
    result = get_best11()

    # -----------------------------------------------------
    # get_best11()에서 받은 결과
    #
    # result['best11']
    #     → 최종 4-3-3 BEST11
    #
    # result['rankings']
    #     → FW / MF / DF / GK 전체 순위
    #
    # result['candidate_count']
    #     → 전체 후보 수
    #
    # result['position_count']
    #     → 포지션별 후보 수
    # -----------------------------------------------------

    context = {
        'best11': result['best11'],
        'rankings': result['rankings'],
        'candidate_count': result['candidate_count'],
        'position_count': result['position_count'],
    }

    # -----------------------------------------------------
    # BEST11 화면으로 전달
    # -----------------------------------------------------
    return render(
        request,
        'player/best11.html',
        context
    )