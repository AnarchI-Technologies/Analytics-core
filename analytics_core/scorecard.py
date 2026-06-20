from __future__ import annotations

from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class EventRecord:
    route: str
    risk: float
    latency_ms: int


@dataclass(frozen=True)
class Scorecard:
    total_events: int
    execution_rate: float
    hold_rate: float
    review_rate: float
    average_risk: float
    average_latency_ms: int


def build_scorecard(events: list[EventRecord]) -> Scorecard:
    if not events:
        return Scorecard(0, 0.0, 0.0, 0.0, 0.0, 0)

    total = len(events)
    risks = [_bounded_risk(event.risk) for event in events]
    latencies = [max(0, event.latency_ms) for event in events]

    return Scorecard(
        total_events=total,
        execution_rate=_rate(events, "execute"),
        hold_rate=_rate(events, "hold"),
        review_rate=_rate(events, "review"),
        average_risk=round(mean(risks), 4),
        average_latency_ms=round(mean(latencies)),
    )


def _rate(events: list[EventRecord], route: str) -> float:
    return round(sum(1 for event in events if event.route == route) / len(events), 4)


def _bounded_risk(risk: float) -> float:
    return min(1.0, max(0.0, risk))

