"""실행: python manage.py test learning.tests

DB를 만들거나 고치지 않습니다. 원래의 계산 의미를 확인하는 검사입니다.
"""
from django.test import SimpleTestCase
from player.scoring import Normalizer, _p90, _rate, metric_weights, default_group_weights
from simulation.tracking_metrics import measure_segments
from team.match_prediction import poisson_probabilities, PredictionUnavailable


class PlayerCalculationTests(SimpleTestCase):
    def test_missing_minutes_are_not_zero_goals(self):
        self.assertIsNone(_p90(3, 0))
        self.assertEqual(_p90(0, 90), 0)
        self.assertEqual(_p90(5, 900), 0.5)

    def test_rate_requires_enough_attempts(self):
        self.assertIsNone(_rate(1, 2, 5))
        self.assertEqual(_rate(3, 5, 5), 0.6)

    def test_missing_value_uses_mean_and_lower_is_better(self):
        norm = Normalizer([{'goals90': 0, 'off90': 0}, {'goals90': 2, 'off90': 4}], ['goals90', 'off90'])
        self.assertEqual(norm.unit('goals90', None), 0.5)
        self.assertEqual(norm.unit('off90', 0), 1)
        self.assertEqual(norm.unit('off90', 4), 0)

    def test_equal_records_are_neutral(self):
        norm = Normalizer([{'goals90': 2}, {'goals90': 2}], ['goals90'])
        self.assertEqual(norm.unit('goals90', 2), 0.5)

    def test_weight_total_and_invalid_input(self):
        self.assertAlmostEqual(sum(metric_weights('FW', default_group_weights('FW')).values()), 100)
        with self.assertRaises(ValueError):
            metric_weights('FW', {})


class TrackingCalculationTests(SimpleTestCase):
    def test_distance_and_speed_units(self):
        result = measure_segments([(5, 1, 18)])
        self.assertEqual(result['total_distance_m'], 5)
        self.assertEqual(result['avg_speed_kmh'], 18)
        self.assertEqual(result['distance_per_minute'], 300)

    def test_sprints_must_be_continuous(self):
        result = measure_segments([(4.2, 0.6, 25.2), (0, 0.2, 0), (4.2, 0.6, 25.2)])
        self.assertEqual(result['sprint_count'], 0)
        result = measure_segments([(3.5, 0.5, 25.2), (3.5, 0.5, 25.2)])
        self.assertEqual(result['sprint_count'], 1)

    def test_empty_tracking_is_rejected(self):
        with self.assertRaises(ValueError):
            measure_segments([])


class PredictionCalculationTests(SimpleTestCase):
    def test_equal_expected_goals_are_symmetric(self):
        result = poisson_probabilities(1.5, 1.5)
        self.assertAlmostEqual(result['H'], result['A'])
        self.assertAlmostEqual(sum(result.values()), 1)

    def test_invalid_expected_goals_are_rejected(self):
        with self.assertRaises(PredictionUnavailable):
            poisson_probabilities(0, 1)
