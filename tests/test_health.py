from fastapi.testclient import TestClient

from app.core.config import Settings, get_settings
from app.main import create_app


def test_health_returns_ok():
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(environment="test")

    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["environment"] == "test"
    assert body["app_name"] == "M&A Due Diligence Platform"
