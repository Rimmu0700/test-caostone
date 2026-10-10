from typing import Protocol

from src.modules.health.schemas import HealthResponse


class DatabaseProbe(Protocol):
    def can_reach_database(self) -> bool: ...


class HealthService:
    def __init__(self, probe: DatabaseProbe) -> None:
        self._probe = probe

    def check(self) -> HealthResponse:
        database_up = self._probe.can_reach_database()
        return HealthResponse(
            status="ok" if database_up else "degraded",
            database="up" if database_up else "down",
        )
