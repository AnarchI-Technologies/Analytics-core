# Analytics Core

Foundational analytics primitives for AnarchI Technologies.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Analytics Core is the measurement layer for AnarchI systems. Its role is to turn raw events, operating signals, and product activity into structured decision support without exposing private runtime data.

## Scope

- Define durable metrics for products, agents, and operations.
- Normalize raw signals into reviewable analytical state.
- Support investor, operator, and builder reporting surfaces.
- Keep sourced facts separate from inferred strategy.

## Current State

This repository is intentionally initialized as a public planning surface. Implementation should be added behind clear module boundaries as analytics sources become ready for public abstraction.

## Design Principles

- Deterministic calculations before model-generated interpretation.
- Reproducible inputs and traceable outputs.
- No secrets, customer data, wallet keys, or private logs in the public repo.
- AI-assisted summaries only after deterministic metrics are computed.

## Planned Structure

```text
analytics-core/
├── metrics/       # Metric definitions and calculation notes
├── pipelines/     # Source normalization and transformations
├── reports/       # Presentation-safe reporting templates
└── tests/         # Fixture-backed validation
```

## Brand

AnarchI builds deterministic systems so deeply compiled that they feel intelligent, while reserving real AI for the moments where it is actually required.