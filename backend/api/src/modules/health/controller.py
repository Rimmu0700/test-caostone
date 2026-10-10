from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.session import get_session
from src.modules.health.repository import HealthRepository
from src.modules.health.schemas import HealthResponse
from src.modules.health.service import HealthService

router = APIRouter(tags=["Health"])


def get_health_service(session: Session = Depends(get_session)) -> HealthService:
    return HealthService(HealthRepository(session))


@router.get("/health", response_model=HealthResponse)
def read_health(service: HealthService = Depends(get_health_service)) -> HealthResponse:
    return service.check()
