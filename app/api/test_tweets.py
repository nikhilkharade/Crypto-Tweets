from fastapi.testclient import TestClient
from app.config import settings
from app.main import app

client = TestClient(app)
print(client)

@app.get("/send-tweets")
def test_send_tweets():
    response = client.get("/send-tweets")
    assert response.status_code == 200