# Event Stream Risk Engine

Event-time risk-scoring reference implementation.

## Design goals
- deterministic scoring baseline
- explicit event-time semantics
- bounded state assumptions
- explainable decisions
- testable late-event behavior

A deterministic baseline remains useful when ML is added: it provides a
fallback, integration oracle, and benchmark for model lift.
