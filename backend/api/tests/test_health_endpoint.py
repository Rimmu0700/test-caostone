from fastapi.testclient import TestClient

from src.main import app


def test_health_endpoint_reports_database_up(db_engine):
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "up"}
