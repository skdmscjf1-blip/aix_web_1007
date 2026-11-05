# 공부 지도: learning/files/simulation/tracking_metrics.py.md
# 역할: 가상 좌표 생성·GPS/이벤트 계산·경기별 저장
"""GPS 계산 전용: 좌표 → 구간 거리·속도 → 선수별 요약. DB 저장은 하지 않습니다."""

import math
from itertools import groupby
from .tracking_spatial import SPATIAL_PARAMETERS, extract_spatial
from .generator import check_document


TRACKING_VERSION = "player-tracking-v1"

PARAMETERS = {
    "high_speed_kmh": 19.8,
    "sprint_speed_kmh": 25.2,
    "minimum_sprint_seconds": 1.0,
}
PARAMETERS.update(SPATIAL_PARAMETERS)


def measure_segments(segments):
    """이동 구간 목록을 합산합니다. 항목 순서는 (거리 m, 시간 초, 속도 km/h)입니다."""
    # 각 항목: 이동 거리(m), 경과 시간(초), 속도(km/h)
    duration = sum(dt for distance, dt, speed in segments)

    if duration <= 0:
        raise ValueError("위치 기록 시간이 부족합니다.")

    total = sum(distance for distance, dt, speed in segments)

    sprint_count = 0
    sprint_distance = 0.0
    sprint_seconds = 0.0

    # 연속으로 스프린트 기준을 넘은 구간을 묶습니다.
    # groupby는 바로 이어진 구간끼리 묶습니다. 끊어진 두 스프린트는 별개입니다.
    groups = groupby(
        segments,
        key=lambda item: (item[2] >= PARAMETERS["sprint_speed_kmh"]),
    )

    for is_sprint, group in groups:
        items = list(group)

        seconds = sum(item[1] for item in items)

        # 1e-9는 소수점 연산의 아주 작은 오차를 허용하는 기존 기준입니다.
        if is_sprint and seconds + 1e-9 >= PARAMETERS["minimum_sprint_seconds"]:
            sprint_count += 1

            sprint_distance += sum(item[0] for item in items)

            sprint_seconds += seconds

    high_speed_distance = sum(
        distance
        for distance, dt, speed in segments
        if speed >= PARAMETERS["high_speed_kmh"]
    )

    return {
        "tracked_seconds": round(duration, 3),
        "total_distance_m": round(total, 3),
        "distance_per_minute": round(
            total / duration * 60,
            3,
        ),
        "avg_speed_kmh": round(
            total / duration * 3.6,
            3,
        ),
        "max_speed_kmh": round(
            max(item[2] for item in segments),
            3,
        ),
        "high_speed_distance_m": round(
            high_speed_distance,
            3,
        ),
        "sprint_count": sprint_count,
        "sprint_distance_m": round(sprint_distance, 3),
        "sprint_seconds": round(sprint_seconds, 3),
    }


def extract_player_tracking(document):
    """연속된 두 장면의 위치 차이를 선수별 이동 구간으로 바꿉니다.

    document는 경기 조건·명단·시간별 좌표가 담긴 사전(dict)입니다.
    이 함수는 계산만 하며, DB 저장은 관리 명령어에서 담당합니다.
    """
    if document.get("is_synthetic") is not True:
        raise ValueError("이 명령어는 더미데이터 전용입니다.")
    check_document(document)

    # 선수마다 (거리, 시간, 속도)를 쌓을 빈 목록을 준비합니다.
    segments = {}
    for player in document["players"]:
        segments[player["player_id"]] = []

    frames = document["frames"]
    # zip은 두 목록에서 하나씩 짝지어 꺼냅니다: (0번, 1번), (1번, 2번) ...
    for before, after in zip(frames, frames[1:]):
        elapsed = after["time_sec"] - before["time_sec"]
        expected_interval = document["sample_interval_sec"]
        if abs(elapsed - expected_interval) > 1e-6:
            raise ValueError("위치 기록 간격에 누락 또는 변경이 있습니다.")

        previous_players = {}
        for player in before["players"]:
            previous_players[player["player_id"]] = player

        for player in after["players"]:
            player_id = player["player_id"]
            old_position = previous_players[player_id]
            horizontal_distance = player["x"] - old_position["x"]
            vertical_distance = player["y"] - old_position["y"]
            # hypot은 가로·세로 이동을 실제 직선 거리로 바꿉니다: 3, 4 → 5m.
            distance = math.hypot(horizontal_distance, vertical_distance)
            speed = distance / elapsed * 3.6  # m/s → km/h
            segments[player_id].append((distance, elapsed, speed))

    spatial = extract_spatial(document)
    result = {}
    for player_id, player_segments in segments.items():
        movement = measure_segments(player_segments)
        # **는 사전의 내용물을 펼칩니다. 기존과 같은 순서로 합칩니다.
        result[player_id] = {**movement, **spatial[player_id]}
    return result
