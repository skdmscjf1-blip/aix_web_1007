from types import SimpleNamespace
from unittest.mock import patch

from django.test import SimpleTestCase

from player.gk_evaluation import match_record, official_metrics
from player.services import calculate_position_scores, get_gk_metrics, GK_WEIGHTS
from player.services import get_filtered_best11
from player.models import Player, PlayerStats
from team.models import Team


class GoalkeeperEvaluationTests(SimpleTestCase):
    def stats(self, name='테스트', pk=1, games=10):
        return SimpleNamespace(
            pk=pk, season=2026, games=games, minutes=900,
            average_rating=7, mom=0, best11_count=0,
            player=SimpleNamespace(name=name, team=SimpleNamespace(team_name='FC서울')),
        )

    def snapshot(self):
        return {'season': 2026, 'league_id': 1, 'records': [{
            'name': '테스트', 'team': '서울', 'games': 10,
            'goals_conceded': 8, 'clean_sheets': 4,
        }]}

    def test_match_requires_same_season_team_and_games(self):
        stats, snapshot = self.stats(), self.snapshot()
        self.assertIsNotNone(match_record(stats, snapshot))
        stats.games = 11
        self.assertIsNone(match_record(stats, snapshot))
        stats.games, stats.season = 10, 2025
        self.assertIsNone(match_record(stats, snapshot))
        stats.season = 2026
        stats.player.team.team_name = '전북현대'
        self.assertIsNone(match_record(stats, snapshot))

    def test_missing_duplicate_or_invalid_records_are_rejected(self):
        stats, snapshot = self.stats(), self.snapshot()
        self.assertIsNone(match_record(stats, None))
        snapshot['records'] *= 2
        self.assertIsNone(match_record(stats, snapshot))
        snapshot = self.snapshot()
        snapshot['records'][0]['clean_sheets'] = 11
        self.assertIsNone(match_record(stats, snapshot))
        snapshot['records'][0]['clean_sheets'] = None
        self.assertIsNone(match_record(stats, snapshot))

    def test_fewer_conceded_and_more_clean_sheets_improve_metrics(self):
        stats = self.stats()
        record = self.snapshot()['records'][0]
        before = official_metrics(stats, record)
        after = official_metrics(stats, dict(record, goals_conceded=0, clean_sheets=5))
        self.assertGreater(after['conceding'], before['conceding'])
        self.assertGreater(after['clean_sheet_rate'], before['clean_sheet_rate'])
        self.assertEqual(after['conceding'], 1)

    def test_complete_snapshot_uses_official_weights(self):
        with patch('player.services.load_snapshot', return_value=self.snapshot()):
            rows = calculate_position_scores([self.stats()], get_gk_metrics, GK_WEIGHTS)
        self.assertEqual(rows[0]['score'], 100)
        self.assertEqual(rows[0]['contributions'], {
            'conceding': 40, 'clean_sheet_rate': 40, 'rating': 20,
        })

    def test_one_missing_record_falls_back_for_entire_cohort(self):
        with patch('player.services.load_snapshot', return_value=self.snapshot()):
            rows = calculate_position_scores(
                [self.stats(), self.stats(name='누락', pk=2)], get_gk_metrics, GK_WEIGHTS,
            )
        for row in rows:
            self.assertEqual(set(row['metrics']), {'rating', 'mom', 'best11', 'minutes'})


class Best11EligibilityTests(SimpleTestCase):
    def candidates(self, minutes):
        team = Team(id=1, team_name='FC서울')
        return [PlayerStats(
            id=i, player=Player(id=i, name=f'GK{i}', position='GK', team=team),
            season=2026, minutes=value, games=10, average_rating=10-i,
        ) for i, value in enumerate(minutes, start=1)]

    def test_short_minutes_can_be_selected_but_never_ranked(self):
        candidates = self.candidates([493, 600, 900])
        with patch('player.services.get_formation_candidates', return_value=candidates), \
             patch('player.services.load_snapshot', return_value=None):
            result = get_filtered_best11()
        self.assertEqual(result['best11']['GK'][0]['stats'].minutes, 493)
        self.assertEqual({row['stats'].minutes for row in result['rankings']['GK']}, {600, 900})
        self.assertEqual(result['position_count']['GK'], 3)

    def test_599_is_excluded_and_600_is_included(self):
        candidates = self.candidates([599, 600])
        with patch('player.services.get_formation_candidates', return_value=candidates), \
             patch('player.services.load_snapshot', return_value=None):
            result = get_filtered_best11(team_id=1)
        self.assertEqual([row['stats'].minutes for row in result['rankings']['GK']], [600])

    def test_filter_does_not_recalculate_scores(self):
        candidates = self.candidates([493, 600, 900])
        with patch('player.services.get_formation_candidates', return_value=candidates), \
             patch('player.services.load_snapshot', return_value=None):
            whole = get_filtered_best11()
            team = get_filtered_best11(team_id=1, formation='5-3-2')
        self.assertEqual(
            [(row['player'].pk, row['score']) for row in whole['rankings']['GK']],
            [(row['player'].pk, row['score']) for row in team['rankings']['GK']],
        )
