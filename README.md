# Analytics Core

Foundational analytics primitives for AnarchI Technologies.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Analytics Core turns raw operating signals into deterministic scorecards. It is intentionally public-safe: examples use synthetic data, calculations are transparent, and model-generated summaries are not allowed until the metrics are computed first.

## What Changed

- Added a small tested Python analytics core.
- Added deterministic scorecard calculations for signal volume, execution rate, hold rate, review rate, and risk.
- Added deterministic operating reports with grade, bottleneck, recommendation, and investor-safe summary.
- Replaced the planning-only README with a usable implementation surface.

## Structure

```text
.
|-- analytics_core/
|   |-- __init__.py
|   |-- operating_report.py
|   `-- scorecard.py
|-- tests/
|   `-- test_scorecard.py
`-- README.md
```

## Verify

```bash
python -m unittest discover -s tests -q
```

## Design Principles

- Sourced facts before inferred strategy.
- Deterministic calculations before language generation.
- Synthetic fixtures for public examples.
- No private logs, customer records, wallet keys, or runtime memory.
