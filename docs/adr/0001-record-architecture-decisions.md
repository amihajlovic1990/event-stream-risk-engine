# ADR 0001: Record architecture decisions

**Status:** Accepted

## Context
Important system decisions cannot always be reconstructed from source code.

## Decision
Use Architecture Decision Records for changes affecting interfaces, state,
security boundaries, reliability, migrations, or material operating cost.

## Consequences
- intent and trade-offs remain reviewable
- migrations retain compatibility context
- future engineers can distinguish constraints from accidents
