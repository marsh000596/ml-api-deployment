from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    assert res.status_code == 200

def test_predict():
    payload = {
        "feature1": 5.1,
        "feature2": 3.5,
        "feature3": 1.4,
        "feature4": 0.2
    }
    res = client.post("/predict", json=payload)
    assert res.status_code == 200
    assert "prediction" in res.json()
