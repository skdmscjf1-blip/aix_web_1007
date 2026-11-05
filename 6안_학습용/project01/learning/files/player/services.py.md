# `player/services.py`

리그 전체 점수·공식 랭킹·구단별 포메이션·레이더를 계산하는 서비스



[실제 코드 열기](../../../player/services.py)



## 이 파일을 읽을 때

1. 입력을 어디서 받는지 찾습니다.

2. 값을 바꾸는 계산과 DB를 읽거나 쓰는 부분을 구분합니다.

3. 마지막 `return` 또는 화면/이벤트 연결을 확인합니다.



## 연결된 Python 모듈

```python

from player.models import PlayerStats

from player import scoring as SC

```

## 함수·클래스 안내

### `number` — 18행

입력 이름: `value`

읽을 때 따라갈 호출(중복 제외): `float`



### `per90` — 32행

입력 이름: `value`, `minutes`

읽을 때 따라갈 호출(중복 제외): `number`



### `success_rate` — 45행

입력 이름: `success`, `attempt`

읽을 때 따라갈 호출(중복 제외): `number`



### `normalize_score` — 60행

입력 이름: `value`, `max_value`

읽을 때 따라갈 호출(중복 제외): `number`



### `get_fw_metrics` — 78행

입력 이름: `stats`

읽을 때 따라갈 호출(중복 제외): `SC.metric_values`



### `get_mf_metrics` — 82행

입력 이름: `stats`

읽을 때 따라갈 호출(중복 제외): `SC.metric_values`



### `get_df_metrics` — 86행

입력 이름: `stats`

읽을 때 따라갈 호출(중복 제외): `SC.metric_values`



### `get_gk_metrics` — 94행

입력 이름: `stats`

읽을 때 따라갈 호출(중복 제외): `SC.metric_values`



### `position_weights` — 110행

관리자 > 점수 기준의 범주 비율을 반영한 컬럼별 가중치.

입력 이름: `position`

읽을 때 따라갈 호출(중복 제외): `SC.metric_weights`



### `calculate_position_scores` — 120행

한 포지션의 선수별 점수를 계산하고 높은 순으로 정렬합니다.

입력 이름: `stats_list`, `metric_function`, `weights`

읽을 때 따라갈 호출(중복 제외): `SC.Normalizer`, `rows.sort`, `rows.append`, `weights.keys`, `weights.items`, `round`, `row['metrics'].get`, `metric_function`, `normalizer.unit`



### `get_best11_candidates` — 172행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `PlayerStats.objects.filter(season=2026, minutes__gte=BEST11_MIN_MINUTES).exclude(player_id__in=EXCLUDED_PLAYER_IDS).select_related`, `list`, `PlayerStats.objects.filter(season=2026, minutes__gte=BEST11_MIN_MINUTES).exclude`, `PlayerStats.objects.filter`



### `get_formation_candidates` — 189행

입력 이름: 

읽을 때 따라갈 호출(중복 제외): `PlayerStats.objects.filter(season=2026, minutes__gte=FORMATION_MIN_MINUTES).exclude(player_id__in=EXCLUDED_PLAYER_IDS).select_related`, `list`, `PlayerStats.objects.filter(season=2026, minutes__gte=FORMATION_MIN_MINUTES).exclude`, `PlayerStats.objects.filter`



### `_rank_by_position` — 203행

공식 BEST11과 구단별 BEST11이 함께 쓰는 포지션별 점수 계산입니다.

입력 이름: `candidates`

읽을 때 따라갈 호출(중복 제외): `players_by_position.items`, `(stats.player.position or '').strip().upper`, `calculate_position_scores`, `players_by_position[position].append`, `position_weights`, `(stats.player.position or '').strip`



### `get_best11` — 224행

리그 공식 BEST11입니다. 점수 기준 450분, 참가 자격 600분을 구분합니다.

입력 이름: 

찾아볼 반환 사전 키(분기·내부 함수 포함): `best11`, `rankings`, `candidate_count`, `position_count`

읽을 때 따라갈 호출(중복 제외): `get_formation_candidates`, `_rank_by_position`, `rankings.items`, `official_rankings.items`, `len`, `sum`, `position_count.values`, `official_rows.append`



### `percentile_score` — 269행

입력 이름: `value`, `values`

읽을 때 따라갈 호출(중복 제외): `number`, `sum`, `round`, `len`



### `get_fw_radar_metrics` — 289행

입력 이름: `stats`

찾아볼 반환 사전 키(분기·내부 함수 포함): `scoring`, `shooting`, `chance`, `dribbling`, `passing`, `duel`

읽을 때 따라갈 호출(중복 제외): `per90`, `success_rate`



### `get_mf_radar_metrics` — 343행

입력 이름: `stats`

찾아볼 반환 사전 키(분기·내부 함수 포함): `attack`, `chance`, `passing`, `dribbling`, `recovery`, `duel`

읽을 때 따라갈 호출(중복 제외): `success_rate`, `per90`



### `get_df_radar_metrics` — 392행

입력 이름: `stats`

찾아볼 반환 사전 키(분기·내부 함수 포함): `defense`, `tackle`, `interception`, `duel`, `buildup`, `activity`

읽을 때 따라갈 호출(중복 제외): `per90`, `success_rate`



### `get_gk_radar_metrics` — 444행

입력 이름: `stats`

찾아볼 반환 사전 키(분기·내부 함수 포함): `passing`, `long_pass`, `recovery`, `clearance`, `playing_time`, `rating`

읽을 때 따라갈 호출(중복 제외): `success_rate`, `per90`, `number`



### `get_position_radar_config` — 485행

입력 이름: `position`

찾아볼 반환 사전 키(분기·내부 함수 포함): `function`, `labels`



### `get_player_radar` — 554행

입력 이름: `player_id`

찾아볼 반환 사전 키(분기·내부 함수 포함): `player`, `stats`, `position`, `best11_score`, `position_rank`, `position_candidate_count`, `radar_labels`, `radar_scores`, `radar`, `raw`

읽을 때 따라갈 호출(중복 제외): `PlayerStats.objects.filter(player_id=player_id, season=2026).select_related('player', 'player__team').first`, `(player.position or '').strip().upper`, `get_position_radar_config`, `get_best11_candidates`, `metric_function`, `list`, `get_best11`, `best11_result['rankings'].get`, `enumerate`, `(candidate.player.position or '').strip().upper`, `player_metrics.keys`, `percentile_score`, `radar_scores.append`, `len`, `PlayerStats.objects.filter(player_id=player_id, season=2026).select_related`, `(player.position or '').strip`, `same_position_stats.append`, `comparison_values.append`, `round`, `(candidate.player.position or '').strip`, `per90`, `success_rate`, `PlayerStats.objects.filter`



### `get_formations` — 757행

입력 이름: 



### `get_filtered_best11` — 778행

전체 리그 기준으로 점수를 계산한 다음, 선택 구단과 포메이션으로 추립니다.

입력 이름: `team_id`, `formation`

찾아볼 반환 사전 키(분기·내부 함수 포함): `best11`, `rankings`, `candidate_count`, `position_count`, `formation`, `formation_count`, `team_id`, `selected_count`, `formation_available`

읽을 때 따라갈 호출(중복 제외): `get_formation_candidates`, `_rank_by_position`, `all_rankings.items`, `rankings.items`, `(stats.player.position or '').strip().upper`, `len`, `int`, `(stats.player.position or '').strip`

