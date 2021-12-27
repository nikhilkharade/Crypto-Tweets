from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

@app.get("/ping")
def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"msg": "pong"}