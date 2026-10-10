from src.modules.health.service import HealthService


class FakeProbe:
    def __init__(self, reachable: bool) -> None:
        self._reachable = reachable

    def can_reach_database(self) -> bool:
        return self._reachable


def test_health_ok_when_database_reachable():
    result = HealthService(FakeProbe(True)).check()
    assert result.status == "ok"
    assert result.database == "up"


def test_health_degraded_when_database_unreachable():
    result = HealthService(FakeProbe(False)).check()
    assert result.status == "degraded"
    assert result.database == "down"
