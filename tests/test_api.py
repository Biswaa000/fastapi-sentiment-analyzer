from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_analyze_sentiment():
    response = client.post("/analyze", json={"text": "I love this!"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "Positive"
