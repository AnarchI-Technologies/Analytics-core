import unittest

from analytics_core import EventRecord, build_operating_report


class OperatingReportTests(unittest.TestCase):
    def test_strong_report_for_low_risk_execution_heavy_events(self):
        report = build_operating_report(
            [
                EventRecord("execute", 0.2, 100),
                EventRecord("execute", 0.3, 150),
                EventRecord("execute", 0.4, 200),
                EventRecord("review", 0.5, 250),
            ]
        )

        self.assertEqual(report.grade, "Strong")
        self.assertEqual(report.bottleneck, "none")
        self.assertIn("Execution rate 75%", report.investor_summary)

    def test_guarded_report_for_hold_pressure(self):
        report = build_operating_report(
            [
                EventRecord("hold", 0.9, 100),
                EventRecord("hold", 0.8, 100),
                EventRecord("execute", 0.2, 100),
            ]
        )

        self.assertEqual(report.grade, "Guarded")
        self.assertEqual(report.bottleneck, "risk_gate_pressure")
        self.assertIn("narrower approval gates", report.recommended_action)

    def test_review_pressure_gets_pre_filter_recommendation(self):
        report = build_operating_report(
            [
                EventRecord("review", 0.4, 100),
                EventRecord("review", 0.5, 100),
                EventRecord("execute", 0.2, 100),
            ]
        )

        self.assertEqual(report.grade, "Needs Review")
        self.assertEqual(report.bottleneck, "operator_review_load")

    def test_no_data_report_is_claim_safe(self):
        report = build_operating_report([])

        self.assertEqual(report.grade, "No Data")
        self.assertEqual(report.bottleneck, "no_signal")
        self.assertIn("before making claims", report.recommended_action)


if __name__ == "__main__":
    unittest.main()
