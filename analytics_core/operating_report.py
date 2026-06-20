from __future__ import annotations

from dataclasses import dataclass

from .scorecard import EventRecord, Scorecard, build_scorecard


@dataclass(frozen=True)
class OperatingReport:
    scorecard: Scorecard
    grade: str
    bottleneck: str
    recommended_action: str
    investor_summary: str


def build_operating_report(events: list[EventRecord]) -> OperatingReport:
    scorecard = build_scorecard(events)
    grade = _grade(scorecard)
    bottleneck = _bottleneck(scorecard)
    recommended_action = _recommended_action(bottleneck)
    investor_summary = (
        f"{grade} operating posture across {scorecard.total_events} synthetic events. "
        f"Execution rate {scorecard.execution_rate:.0%}; hold rate {scorecard.hold_rate:.0%}; "
        f"review rate {scorecard.review_rate:.0%}; average risk {scorecard.average_risk:.2f}."
    )

    return OperatingReport(
        scorecard=scorecard,
        grade=grade,
        bottleneck=bottleneck,
        recommended_action=recommended_action,
        investor_summary=investor_summary,
    )


def _grade(scorecard: Scorecard) -> str:
    if scorecard.total_events == 0:
        return "No Data"
    if scorecard.hold_rate >= 0.35 or scorecard.average_risk >= 0.7:
        return "Guarded"
    if scorecard.review_rate >= 0.4 or scorecard.average_latency_ms >= 750:
        return "Needs Review"
    if scorecard.execution_rate >= 0.65 and scorecard.average_risk <= 0.45:
        return "Strong"
    return "Stable"


def _bottleneck(scorecard: Scorecard) -> str:
    if scorecard.total_events == 0:
        return "no_signal"
    if scorecard.hold_rate >= 0.35:
        return "risk_gate_pressure"
    if scorecard.review_rate >= 0.4:
        return "operator_review_load"
    if scorecard.average_latency_ms >= 750:
        return "latency_drag"
    if scorecard.execution_rate < 0.35:
        return "low_execution_throughput"
    return "none"


def _recommended_action(bottleneck: str) -> str:
    actions = {
        "no_signal": "Add synthetic fixtures or reviewed source telemetry before making claims.",
        "risk_gate_pressure": "Split high-risk routes into narrower approval gates.",
        "operator_review_load": "Add deterministic pre-filters before operator review.",
        "latency_drag": "Profile slow routes and separate batch work from live decision paths.",
        "low_execution_throughput": "Audit routing thresholds and identify safe automation candidates.",
        "none": "Maintain current deterministic operating posture and continue evidence capture.",
    }
    return actions[bottleneck]
