import io

import pytest
from fastapi.testclient import TestClient

from app.core.config import Settings, get_settings
from app.main import create_app


@pytest.fixture()
def client(tmp_path):
    app = create_app()
    app.dependency_overrides[get_settings] = lambda: Settings(
        environment="test",
        vault_dir=tmp_path / "vault",
    )
    return TestClient(app)


def test_upload_pdf_succeeds(client, tmp_path):
    pdf_bytes = b"%PDF-1.4 fake pdf content"
    response = client.post(
        "/documents/upload",
        files={"file": ("report.pdf", io.BytesIO(pdf_bytes), "application/pdf")},
    )
    assert response.status_code == 201
    body = response.json()
    assert body["filename"] == "report.pdf"
    assert body["status"] == "uploaded"
    assert body["saved_path"].endswith("report.pdf")


def test_upload_non_pdf_rejected(client):
    response = client.post(
        "/documents/upload",
        files={"file": ("notes.txt", io.BytesIO(b"hello"), "text/plain")},
    )
    assert response.status_code == 400
    assert "PDF" in response.json()["detail"]
