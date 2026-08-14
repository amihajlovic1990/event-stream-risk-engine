from datetime import datetime, timedelta, timezone
from risk_engine.scoring import Event, score

NOW = datetime(2026, 1, 1, tzinfo=timezone.utc)


def test_high_amount_explained():
    result = score(Event("x", NOW, 20_000, "AE"), [], NOW)
    assert result.score == 40
    assert result.reasons == ("high_amount",)


def test_old_events_do_not_inflate_velocity():
    old = [Event("x", NOW - timedelta(hours=1), 1, "AE") for _ in range(10)]
    result = score(Event("x", NOW, 1, "AE"), old, NOW)
    assert "high_velocity" not in result.reasons
