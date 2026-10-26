from player.models import PlayerStats


# =========================================================
# BEST11 최소 출전시간
# =========================================================

MIN_MINUTES = 600


# =========================================================
# 숫자 안전 변환
#
# None이나 이상한 값이 들어와도
# 계산 중 오류가 나지 않도록 0으로 처리
# =========================================================

def number(value):

    if value is None:
        return 0.0

    try:
        return float(value)

    except (TypeError, ValueError):
        return 0.0


# =========================================================
# 90분당 기록 계산
#
# 예)
# 1800분 출전
# 10골
#
# 10 / 1800 * 90
# = 0.5골/90분
# =========================================================

def per90(value, minutes):

    value = number(value)
    minutes = number(minutes)

    if minutes <= 0:
        return 0.0

    return value / minutes * 90


# =========================================================
# 성공률 계산
#
# 성공 / 시도 * 100
#
# 예)
# 패스 성공 80
# 패스 시도 100
#
# = 80%
# =========================================================

def success_rate(success, attempt):

    success = number(success)
    attempt = number(attempt)

    if attempt <= 0:
        return 0.0

    return success / attempt * 100


# =========================================================
# 최고값 기준 점수 변환
#
# 현재 1차 BEST11에서 사용한 방식
#
# 최고 선수 = 100점
# =========================================================

def normalize_score(value, max_value):

    value = number(value)
    max_value = number(max_value)

    if max_value <= 0:
        return 0.0

    return value / max_value * 100


# =========================================================
# FW 평가 지표
# =========================================================

def get_fw_metrics(stats):

    return {

        'goals': per90(
            stats.goals,
            stats.minutes
        ),

        'assists': per90(
            stats.assists,
            stats.minutes
        ),

        'shots_on_target': per90(
            stats.shots_on_target,
            stats.minutes
        ),

        'shots': per90(
            stats.shots,
            stats.minutes
        ),

        'key_passes': per90(
            stats.key_passes,
            stats.minutes
        ),

        'dribble': per90(
            stats.dribble_success,
            stats.minutes
        ),
    }


# =========================================================
# MF 평가 지표
# =========================================================

def get_mf_metrics(stats):

    return {

        'assists': per90(
            stats.assists,
            stats.minutes
        ),

        'key_passes': per90(
            stats.key_passes,
            stats.minutes
        ),

        'pass_rate': success_rate(
            stats.pass_success,
            stats.pass_attempt
        ),

        'goals': per90(
            stats.goals,
            stats.minutes
        ),

        'recoveries': per90(
            stats.recoveries,
            stats.minutes
        ),

        'interceptions': per90(
            stats.interceptions,
            stats.minutes
        ),

        'dribble': per90(
            stats.dribble_success,
            stats.minutes
        ),
    }


# =========================================================
# DF 평가 지표
# =========================================================

def get_df_metrics(stats):

    return {

        'clearances': per90(
            stats.clearances,
            stats.minutes
        ),

        'interceptions': per90(
            stats.interceptions,
            stats.minutes
        ),

        'recoveries': per90(
            stats.recoveries,
            stats.minutes
        ),

        'tackle': per90(
            stats.tackle_success,
            stats.minutes
        ),

        'aerial_duel': per90(
            stats.aerial_duel_success,
            stats.minutes
        ),

        'ground_duel': per90(
            stats.ground_duel_success,
            stats.minutes
        ),

        'defensive_blocks': per90(
            stats.defensive_blocks,
            stats.minutes
        ),

        'blocks': per90(
            stats.blocks,
            stats.minutes
        ),
    }


# =========================================================
# GK 평가 지표
#
# 현재는 임시 평가
#
# 선방 / 실점 / 클린시트 데이터가 없기 때문에
#
# 평균평점
# MOM
# BEST11 선정
# 출전시간
#
# 사용
# =========================================================

def get_gk_metrics(stats):

    return {

        'rating': number(
            stats.average_rating
        ),

        'mom': per90(
            stats.mom,
            stats.minutes
        ),

        'best11': per90(
            stats.best11_count,
            stats.minutes
        ),

        'minutes': number(
            stats.minutes
        ),
    }


# =========================================================
# 포지션별 가중치
# =========================================================

FW_WEIGHTS = {

    'goals': 35,
    'assists': 20,
    'shots_on_target': 15,
    'shots': 10,
    'key_passes': 10,
    'dribble': 10,
}


MF_WEIGHTS = {

    'assists': 20,
    'key_passes': 20,
    'pass_rate': 20,
    'goals': 15,
    'recoveries': 10,
    'interceptions': 10,
    'dribble': 5,
}


DF_WEIGHTS = {

    'clearances': 20,
    'interceptions': 20,
    'recoveries': 15,
    'tackle': 15,
    'aerial_duel': 10,
    'ground_duel': 10,
    'defensive_blocks': 5,
    'blocks': 5,
}


# GK는 아직 임시 기준
GK_WEIGHTS = {

    'rating': 50,
    'mom': 15,
    'best11': 25,
    'minutes': 10,
}


# =========================================================
# 한 포지션의 선수들을 점수화
# =========================================================

def calculate_position_scores(
    stats_list,
    metric_function,
    weights
):

    rows = []

    # -----------------------------------------------------
    # 1. 선수별 실제 기록 계산
    # -----------------------------------------------------

    for stats in stats_list:

        metrics = metric_function(
            stats
        )

        rows.append({

            'stats': stats,

            'player': stats.player,

            'metrics': metrics,
        })

    # -----------------------------------------------------
    # 2. 각 평가항목의 최고값 찾기
    #
    # 예)
    #
    # FW 득점/90 최고 = 0.83
    # FW 도움/90 최고 = 0.55
    # ...
    # -----------------------------------------------------

    max_values = {}

    for metric_name in weights.keys():

        values = [

            row['metrics'][metric_name]

            for row in rows
        ]

        if values:

            max_values[metric_name] = max(
                values
            )

        else:

            max_values[metric_name] = 0

    # -----------------------------------------------------
    # 3. 점수 계산
    # -----------------------------------------------------

    for row in rows:

        total_score = 0.0

        normalized = {}

        contributions = {}

        for metric_name, weight in weights.items():

            raw_value = (
                row['metrics'][metric_name]
            )

            max_value = (
                max_values[metric_name]
            )

            # 0~100점
            score = normalize_score(
                raw_value,
                max_value
            )

            # 가중치 적용
            contribution = (
                score
                * weight
                / 100
            )

            normalized[metric_name] = score

            contributions[metric_name] = (
                contribution
            )

            total_score += contribution

        row['normalized'] = normalized

        row['contributions'] = contributions

        row['score'] = round(
            total_score,
            2
        )

    # -----------------------------------------------------
    # 4. 점수가 높은 순서로 정렬
    # -----------------------------------------------------

    rows.sort(
        key=lambda row: row['score'],
        reverse=True
    )

    return rows


# =========================================================
# 2026 BEST11 후보 가져오기
#
# 중요:
# 기존 DB 전용 9명은 제외해야 함.
#
# 현재 데이터 구조에서는
# JSON 선수성적과 일치하는 현재 선수만 사용해야 하므로
# 우선 DB 전용 선수 ID를 명시적으로 제외한다.
#
# 이후 데이터 구조를 정리하면
# is_active / current_roster 같은 컬럼으로 개선 가능.
# =========================================================

def get_best11_candidates():

    # -----------------------------------------------------
    # 현재 확인된 DB 전용 2026 성적 선수
    # -----------------------------------------------------

    excluded_player_ids = [
        232,  # FC안양 토마스
        222,  # FC안양 황병근
        72,   # 광주FC 박정인
        82,   # 김천상무 백종범
        111,  # 김천상무 이건희
        276,  # 울산HD 이민혁
        290,  # 인천유나이티드 이상현
        383,  # 제주SK FC 기티스
        380,  # 제주SK FC 오재혁
    ]

    stats_list = (
        PlayerStats.objects
        .filter(
            season=2026,
            minutes__gte=MIN_MINUTES
        )
        .exclude(
            player_id__in=excluded_player_ids
        )
        .select_related(
            'player',
            'player__team'
        )
    )

    return list(
        stats_list
    )


# =========================================================
# 실제 BEST11 계산
#
# 이 함수 하나를 views.py에서 호출하게 됨.
# =========================================================

def get_best11():

    # =====================================================
    # 후보 가져오기
    # =====================================================

    candidates = (
        get_best11_candidates()
    )

    # =====================================================
    # 포지션별 분리
    # =====================================================

    gk_list = []
    df_list = []
    mf_list = []
    fw_list = []

    for stats in candidates:

        position = (
            stats.player.position
            or ''
        ).strip().upper()

        if position == 'GK':

            gk_list.append(
                stats
            )

        elif position == 'DF':

            df_list.append(
                stats
            )

        elif position == 'MF':

            mf_list.append(
                stats
            )

        elif position == 'FW':

            fw_list.append(
                stats
            )

    # =====================================================
    # 포지션별 점수 계산
    # =====================================================

    fw_ranking = calculate_position_scores(
        fw_list,
        get_fw_metrics,
        FW_WEIGHTS
    )

    mf_ranking = calculate_position_scores(
        mf_list,
        get_mf_metrics,
        MF_WEIGHTS
    )

    df_ranking = calculate_position_scores(
        df_list,
        get_df_metrics,
        DF_WEIGHTS
    )

    gk_ranking = calculate_position_scores(
        gk_list,
        get_gk_metrics,
        GK_WEIGHTS
    )

    # =====================================================
    # 4-3-3 BEST11
    # =====================================================

    best11 = {

        'FW': fw_ranking[:3],

        'MF': mf_ranking[:3],

        'DF': df_ranking[:4],

        'GK': gk_ranking[:1],
    }

    # =====================================================
    # 화면에서 TOP10도 사용할 수 있게 반환
    # =====================================================

    rankings = {

        'FW': fw_ranking,

        'MF': mf_ranking,

        'DF': df_ranking,

        'GK': gk_ranking,
    }

    return {

        'best11': best11,

        'rankings': rankings,

        'candidate_count': len(
            candidates
        ),

        'position_count': {

            'FW': len(fw_list),

            'MF': len(mf_list),

            'DF': len(df_list),

            'GK': len(gk_list),
        }
    }