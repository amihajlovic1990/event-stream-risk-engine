from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen=True)
class Event:
    entity_id: str
    occurred_at: datetime
    amount: float
    country: str


@dataclass(frozen=True)
class Decision:
    score: int
    reasons: tuple[str, ...]


def score(event: Event, history: list[Event], now: datetime) -> Decision:
    reasons = []
    value = 0
    start = now - timedelta(minutes=10)
    window = [e for e in history if start <= e.occurred_at <= now]

    if len(window) >= 5:
        value += 35
        reasons.append("high_velocity")
    if event.amount >= 10_000:
        value += 40
        reasons.append("high_amount")
    countries = {e.country for e in window}
    if countries and event.country not in countries:
        value += 25
        reasons.append("country_change")

    return Decision(min(value, 100), tuple(reasons))
