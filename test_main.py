from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate():
    response = client.post("/generate", json={"text": "hello"})
    assert response.status_code == 200
    assert "checksum" in response.json()