from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")  # type: ignore
    assert response.status_code == 200  # type: ignore
    assert response.json() == {"msg": "Hello World"}  # type: ignore
