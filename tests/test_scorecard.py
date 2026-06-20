import unittest

from analytics_core import EventRecord, build_scorecard


class ScorecardTests(unittest.TestCase):
    def test_empty_scorecard_is_zeroed(self):
        card = build_scorecard([])

        self.assertEqual(card.total_events, 0)
        self.assertEqual(card.execution_rate, 0.0)

    def test_builds_route_rates_and_averages(self):
        card = build_scorecard(
            [
                EventRecord("execute", 0.2, 100),
                EventRecord("execute", 0.4, 200),
                EventRecord("hold", 0.9, 300),
                EventRecord("review", 0.5, 400),
            ]
        )

        self.assertEqual(card.total_events, 4)
        self.assertEqual(card.execution_rate, 0.5)
        self.assertEqual(card.hold_rate, 0.25)
        self.assertEqual(card.review_rate, 0.25)
        self.assertEqual(card.average_risk, 0.5)
        self.assertEqual(card.average_latency_ms, 250)

    def test_bounds_risk_and_latency(self):
        card = build_scorecard([EventRecord("execute", 2.0, -50)])

        self.assertEqual(card.average_risk, 1.0)
        self.assertEqual(card.average_latency_ms, 0)


if __name__ == "__main__":
    unittest.main()

