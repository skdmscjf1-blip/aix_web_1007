# 공부 지도: learning/files/player/scoring.py.md
# 역할: 선수 기록·공통 점수·BEST11·연구실
"""BEST11 · 감독 연구실 · 승부예측이 함께 쓰는 '통합 선수 점수'의 컬럼과 범주.

- 포지션마다 컬럼(기존 기록 + 추가 컬럼)을 큰 범주 4~6개로 묶는다.
- 범주 비율(가중치)은 관리자 > 점수 기준에서 기본값을, BEST11 화면의 감독 연구실에서 내 설정을 바꿀 수 있다.
- 범주 안의 컬럼은 같은 비중이다 (범주 비율 ÷ 컬럼 수).
- 점수 계산(정규화): 같은 포지션 비교 대상 안에서 (값 - 최저) ÷ (최고 - 최저) → 0~1.
  '적을수록 좋은' 컬럼(실점·오프사이드·경고 등)은 1에서 뺀다. 값이 없는 선수는 비교 대상 평균을 쓴다.
- '가상' 표시 컬럼은 team/virtual_stats.py 의 가상 데이터다 (실제 기록 아님).
"""

import math

PER90 = 'per90'
RATE = 'rate'
VALUE = 'value'


def _p90(value, minutes):
    """90분당 기록. 예: 5골 / 900분 * 90 = 0.5골."""
    if not minutes or minutes <= 0:
        # 0이 아니라 None: 출전이 없어 계산할 수 없다는 뜻입니다.
        return None
    record_per_minute = value / minutes
    return record_per_minute * 90


def _rate(success, attempt, minimum):
    """시도 수가 기준 이상일 때만 성공 비율(0~1)을 계산합니다."""
    if not attempt or attempt < minimum:
        return None
    return success / attempt


def _full_match_rate(s):
    """총 출전분이 모든 경기를 90분씩 뛰었을 때의 몇 배인지 구합니다."""
    games = s.games or 0
    if not games:
        return None
    possible_minutes = games * 90
    return min(1.0, s.minutes / possible_minutes)


def _age_fit(s):
    """기존 나이 규칙을 유지합니다. 26~30세는 0, 벗어난 만큼 음수입니다.

    실제 경기력으로 검증한 최적 나이 기준이라는 뜻은 아닙니다.
    """
    from team.virtual_stats import player_age

    age = player_age(s.player)
    if not age:
        return None
    distance_from_28 = abs(age - 28)
    distance_from_range = max(0, distance_from_28 - 2)
    return -distance_from_range


def _cards_90(s):
    return _p90(s.yellow_cards + 2 * s.red_cards, s.minutes)


def _v(key):
    """가상 기록에서 특정 컬럼을 꺼내는 함수를 만듭니다.

    예: _v('distance_km_90')는 해당 거리 값을 읽는 함수입니다.
    """

    def read_virtual_value(stats, virtual_data):
        return virtual_data.get(key)

    return read_virtual_value


# 키: (이름, 계산(stats, 가상데이터) -> 값, 높을수록 좋음?, 단위, 시즌 합계 필드, 가상?)
METRIC_DEFS = {
    'goals90': (
        '득점',
        lambda s, v: _p90(s.goals, s.minutes),
        True,
        PER90,
        'goals',
        False,
    ),
    'sot90': (
        '유효슈팅',
        lambda s, v: _p90(s.shots_on_target, s.minutes),
        True,
        PER90,
        'shots_on_target',
        False,
    ),
    'shots90': (
        '슈팅',
        lambda s, v: _p90(s.shots, s.minutes),
        True,
        PER90,
        'shots',
        False,
    ),
    'shot_acc': (
        '슈팅 정확도',
        lambda s, v: _rate(s.shots_on_target, s.shots, 5),
        True,
        RATE,
        None,
        False,
    ),
    'conv': (
        '득점 전환율',
        lambda s, v: _rate(s.goals, s.shots, 5),
        True,
        RATE,
        None,
        False,
    ),
    'box': (
        '박스 안 슈팅 비율',
        lambda s, v: _rate(s.shots_inside_box, s.shots, 5),
        True,
        RATE,
        None,
        False,
    ),
    'ast90': (
        '도움',
        lambda s, v: _p90(s.assists, s.minutes),
        True,
        PER90,
        'assists',
        False,
    ),
    'kp90': (
        '키패스',
        lambda s, v: _p90(s.key_passes, s.minutes),
        True,
        PER90,
        'key_passes',
        False,
    ),
    'drb90': (
        '드리블 성공',
        lambda s, v: _p90(s.dribble_success, s.minutes),
        True,
        PER90,
        'dribble_success',
        False,
    ),
    'drb_rate': (
        '드리블 성공률',
        lambda s, v: _rate(s.dribble_success, s.dribble_attempt, 5),
        True,
        RATE,
        None,
        False,
    ),
    'fw90': (
        '피파울',
        lambda s, v: _p90(s.fouls_won, s.minutes),
        True,
        PER90,
        'fouls_won',
        False,
    ),
    'aer_rate': (
        '공중볼 성공률',
        lambda s, v: _rate(s.aerial_duel_success, s.aerial_duel_attempt, 5),
        True,
        RATE,
        None,
        False,
    ),
    'aer90': (
        '공중볼 성공',
        lambda s, v: _p90(s.aerial_duel_success, s.minutes),
        True,
        PER90,
        'aerial_duel_success',
        False,
    ),
    'gnd90': (
        '지상볼 성공',
        lambda s, v: _p90(s.ground_duel_success, s.minutes),
        True,
        PER90,
        'ground_duel_success',
        False,
    ),
    'gnd_rate': (
        '지상볼 성공률',
        lambda s, v: _rate(s.ground_duel_success, s.ground_duel_attempt, 5),
        True,
        RATE,
        None,
        False,
    ),
    'tkl90': (
        '태클 성공',
        lambda s, v: _p90(s.tackle_success, s.minutes),
        True,
        PER90,
        'tackle_success',
        False,
    ),
    'tkl_rate': (
        '태클 성공률',
        lambda s, v: _rate(s.tackle_success, s.tackle_attempt, 5),
        True,
        RATE,
        None,
        False,
    ),
    'dist': ('활동량 km(가상)', _v('distance_km_90'), True, PER90, None, True),
    'spr': ('스프린트(가상)', _v('sprints_90'), True, PER90, None, True),
    'full': (
        '풀타임 소화율',
        lambda s, v: _full_match_rate(s),
        True,
        RATE,
        None,
        False,
    ),
    'height': ('키', lambda s, v: s.player.height or None, True, VALUE, None, False),
    'weight': (
        '몸무게',
        lambda s, v: s.player.weight or None,
        True,
        VALUE,
        None,
        False,
    ),
    'off90': (
        '오프사이드',
        lambda s, v: _p90(s.offsides, s.minutes),
        False,
        PER90,
        'offsides',
        False,
    ),
    'cards90': (
        '경고·퇴장',
        lambda s, v: _cards_90(s),
        False,
        PER90,
        'yellow_cards',
        False,
    ),
    'disc90': (
        '파울·경고',
        lambda s, v: _p90(s.fouls + 3 * s.yellow_cards + 6 * s.red_cards, s.minutes),
        False,
        PER90,
        'fouls',
        False,
    ),
    'age': ('나이(전성기 26~30세)', lambda s, v: _age_fit(s), True, VALUE, None, False),
    'pass_rate': (
        '패스 정확도',
        lambda s, v: _rate(s.pass_success, s.pass_attempt, 30),
        True,
        RATE,
        None,
        False,
    ),
    'fwd_rate': (
        '전진 패스 성공률',
        lambda s, v: _rate(s.forward_pass_success, s.forward_pass_attempt, 15),
        True,
        RATE,
        None,
        False,
    ),
    'att3_rate': (
        '공격 진영 패스 성공률',
        lambda s, v: _rate(
            s.attacking_third_pass_success, s.attacking_third_pass_attempt, 15
        ),
        True,
        RATE,
        None,
        False,
    ),
    'long_rate': (
        '롱패스 성공률',
        lambda s, v: _rate(s.long_pass_success, s.long_pass_attempt, 10),
        True,
        RATE,
        None,
        False,
    ),
    'cross_rate': (
        '크로스 성공률',
        lambda s, v: _rate(s.cross_success, s.cross_attempt, 5),
        True,
        RATE,
        None,
        False,
    ),
    'def3_rate': (
        '수비 진영 패스 성공률',
        lambda s, v: _rate(
            s.defensive_third_pass_success, s.defensive_third_pass_attempt, 15
        ),
        True,
        RATE,
        None,
        False,
    ),
    'rec90': (
        '볼 회수',
        lambda s, v: _p90(s.recoveries, s.minutes),
        True,
        PER90,
        'recoveries',
        False,
    ),
    'int90': (
        '인터셉트',
        lambda s, v: _p90(s.interceptions, s.minutes),
        True,
        PER90,
        'interceptions',
        False,
    ),
    'clr90': (
        '클리어링',
        lambda s, v: _p90(s.clearances, s.minutes),
        True,
        PER90,
        'clearances',
        False,
    ),
    'dblk90': (
        '수비 차단',
        lambda s, v: _p90(s.defensive_blocks, s.minutes),
        True,
        PER90,
        'defensive_blocks',
        False,
    ),
    'blk90': (
        '블록',
        lambda s, v: _p90(s.blocks, s.minutes),
        True,
        PER90,
        'blocks',
        False,
    ),
    'miss90': (
        '볼 미스',
        lambda s, v: _p90(s.ball_misses, s.minutes),
        False,
        PER90,
        'ball_misses',
        False,
    ),
    'rating': (
        '평균 평점',
        lambda s, v: s.average_rating or None,
        True,
        VALUE,
        None,
        False,
    ),
    'best11': (
        '베스트11 선정(누적)',
        lambda s, v: float(s.best11_count or 0),
        True,
        VALUE,
        'best11_count',
        False,
    ),
    'mom': ('MOM(누적)', lambda s, v: float(s.mom or 0), True, VALUE, 'mom', False),
    'minutes': (
        '출전시간',
        lambda s, v: float(s.minutes or 0),
        True,
        VALUE,
        None,
        False,
    ),
    'save_rate': ('선방률(가상)', _v('save_rate'), True, RATE, None, True),
    'saves90': ('선방(가상)', _v('saves_90'), True, PER90, None, True),
    'conc90': ('실점(가상)', _v('conceded_90'), False, PER90, None, True),
    'cs_rate': ('무실점 비율(가상)', _v('clean_sheet_rate'), True, RATE, None, True),
    'claims': (
        '펀칭+캐칭(가상)',
        lambda s, v: (v['punches_90'] + v['catches_90']) if 'punches_90' in v else None,
        True,
        PER90,
        None,
        True,
    ),
}

# 포지션별 범주: (범주 키, 이름, 기본 비율, [컬럼 키])
GROUPS = {
    'FW': [
        (
            'finishing',
            '득점력',
            45,
            ['goals90', 'sot90', 'shots90', 'shot_acc', 'conv', 'box'],
        ),
        ('creation', '찬스 창출', 22, ['ast90', 'kp90']),
        ('dribbling', '개인기·돌파', 13, ['drb90', 'drb_rate', 'fw90']),
        (
            'physical',
            '피지컬·체력',
            12,
            ['aer_rate', 'dist', 'spr', 'full', 'height', 'weight'],
        ),
        ('discipline', '규율·경험', 8, ['off90', 'cards90', 'age']),
    ],
    'MF': [
        ('attack', '공격·찬스 창출', 38, ['ast90', 'kp90', 'goals90']),
        (
            'passing',
            '패스·빌드업',
            18,
            ['pass_rate', 'fwd_rate', 'att3_rate', 'long_rate', 'cross_rate'],
        ),
        ('defending', '수비 가담', 18, ['rec90', 'int90', 'tkl_rate']),
        ('dribbling', '개인기', 8, ['drb90', 'drb_rate', 'miss90']),
        ('physical', '피지컬·체력', 12, ['dist', 'spr', 'full', 'height', 'weight']),
        ('discipline', '규율·경험', 6, ['cards90', 'age']),
    ],
    'DF': [
        ('actions', '수비 액션', 45, ['clr90', 'int90', 'rec90', 'dblk90', 'blk90']),
        (
            'duels',
            '경합·태클',
            28,
            ['tkl90', 'tkl_rate', 'aer90', 'aer_rate', 'gnd90', 'gnd_rate'],
        ),
        ('buildup', '빌드업', 9, ['def3_rate', 'long_rate']),
        ('physical', '피지컬·체력', 12, ['dist', 'spr', 'full', 'height', 'weight']),
        ('discipline', '규율·경험', 6, ['disc90', 'age']),
    ],
    'GK': [
        ('rating', '경기 평가', 55, ['rating', 'best11', 'mom']),
        ('shotstop', '선방·실점', 20, ['save_rate', 'saves90', 'conc90', 'cs_rate']),
        ('claims', '공중볼 처리', 5, ['claims']),
        ('buildup', '빌드업', 8, ['pass_rate', 'long_rate']),
        ('fitness', '출전·피지컬', 12, ['minutes', 'full', 'height', 'weight', 'age']),
    ],
}
POSITIONS = ('FW', 'MF', 'DF', 'GK')

# 예전 지표 이름 → 새 컬럼 (감독 연구실 프리셋·상대 맞춤이 예전 이름을 쓴다)
OLD_KEYS = {
    'goals': ['goals90'],
    'assists': ['ast90'],
    'shots_on_target': ['sot90'],
    'shots': ['shots90'],
    'key_passes': ['kp90'],
    'dribble': ['drb90', 'drb_rate'],
    'pass_rate': ['pass_rate', 'fwd_rate', 'att3_rate'],
    'recoveries': ['rec90'],
    'interceptions': ['int90'],
    'clearances': ['clr90'],
    'tackle': ['tkl90', 'tkl_rate'],
    'aerial_duel': ['aer90', 'aer_rate'],
    'ground_duel': ['gnd90', 'gnd_rate'],
    'defensive_blocks': ['dblk90'],
    'blocks': ['blk90'],
    'rating': ['rating'],
    'mom': ['mom'],
    'best11': ['best11'],
    'minutes': ['minutes'],
}

LOWER_BETTER = {k for k, d in METRIC_DEFS.items() if not d[2]}
# 소표본 보정(출전 적은 선수를 평균 쪽으로)에서 빼는 컬럼: 신체·나이·출전 관련
NO_SHRINK = {'minutes', 'height', 'weight', 'age', 'full', 'best11', 'mom'}


def label(key):
    """컬럼 키를 화면 이름으로 바꿉니다. 모르는 키는 그대로 돌려줍니다."""
    if key not in METRIC_DEFS:
        return key
    return METRIC_DEFS[key][0]


def metric_keys(pos):
    """한 포지션의 범주를 차례대로 돌며 컬럼 키를 모읍니다."""
    keys = []
    for group_key, group_name, weight, metric_names in GROUPS[pos]:
        for metric_name in metric_names:
            keys.append(metric_name)
    return keys


def group_of(pos):
    """컬럼이 어느 범주에 속하는지 찾아볼 사전을 만듭니다."""
    result = {}
    for group_key, group_name, weight, metric_names in GROUPS[pos]:
        for metric_name in metric_names:
            result[metric_name] = group_key
    return result


def default_group_weights(pos):
    """예: 공격수의 {'finishing': 45.0, ...}를 만듭니다."""
    weights = {}
    for group_key, group_name, weight, metric_names in GROUPS[pos]:
        weights[group_key] = float(weight)
    return weights


def group_weights(pos):
    """범주 비율: 관리자 > 점수 기준에 저장한 값이 있으면 그것, 없으면 기본값."""
    base = default_group_weights(pos)
    try:
        from manager import config

        return config.group_weights_for(pos, base)
    except Exception:
        return base


def metric_weights(pos, groups=None):
    """범주 비중을 합계 100으로 맞추고, 각 컬럼에 똑같이 나눕니다."""
    # 1. 직접 넘겨받은 설정이 없으면 관리자 기본 설정을 읽습니다.
    if groups is None:
        groups = group_weights(pos)

    # 2. 알려진 범주의 숫자만 읽습니다. 생략한 범주는 기존처럼 0입니다.
    values = {}
    for group_key, group_name, default_weight, keys in GROUPS[pos]:
        values[group_key] = float(groups.get(group_key, 0.0))

    for value in values.values():
        if not math.isfinite(value) or value < 0:
            raise ValueError('범주 비율은 유한한 0 이상의 숫자여야 합니다.')

    total = sum(values.values())
    if not math.isfinite(total) or total <= 0:
        raise ValueError('범주 비율 합은 유한한 양수여야 합니다.')

    # 3. 연산 순서도 유지합니다: 범주 / 전체 * 100 / 컬럼 개수.
    weights = {}
    for group_key, group_name, default_weight, keys in GROUPS[pos]:
        weight_per_metric = values[group_key] / total * 100 / len(keys)
        for key in keys:
            weights[key] = weight_per_metric
    return weights


def metric_values(stats, pos):
    """한 선수의 시즌 기록과 가상 기록으로 평가 항목 값을 만듭니다."""
    from team.virtual_stats import for_player

    virtual_data = for_player(stats.player_id)
    values = {}
    for key in metric_keys(pos):
        # METRIC_DEFS의 두 번째 칸에는 계산할 함수가 있습니다.
        calculate = METRIC_DEFS[key][1]
        try:
            values[key] = calculate(stats, virtual_data)
        except (TypeError, ZeroDivisionError):
            values[key] = None
    return values


class Normalizer:
    """정규화 도구: 같은 포지션에서 각 값의 위치를 0~1로 나타냅니다.

    lo/hi/mean은 외부 코드에서도 쓰므로 이름을 유지합니다.
    lo = 최저값, hi = 최고값, mean = 평균값입니다.
    """

    def __init__(self, values_list, keys):
        self.lo = {}
        self.hi = {}
        self.mean = {}
        for key in keys:
            available_values = []
            for values in values_list:
                if values.get(key) is not None:
                    available_values.append(values[key])
            if available_values:
                self.lo[key] = min(available_values)
                self.hi[key] = max(available_values)
                self.mean[key] = sum(available_values) / len(available_values)

    def fill(self, k, x):
        """기록이 없으면 비교 집단 평균으로 채웁니다. 평균도 없으면 None."""
        if x is not None:
            return x
        return self.mean.get(k)

    def unit(self, k, x):
        """비교 구간 중 위치를 반환합니다. 0.5는 성공률이 아닌 중간 위치입니다."""
        x = self.fill(k, x)
        if x is None or k not in self.lo:
            return 0.5
        lowest = self.lo[k]
        highest = self.hi[k]
        if highest == lowest:
            normalized = 0.5
        else:
            normalized = (x - lowest) / (highest - lowest)
            normalized = max(0.0, min(1.0, normalized))
        if k in LOWER_BETTER:
            return 1 - normalized
        return normalized
