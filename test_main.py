from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API is running!"}


def test_predict_price():

    payload = {
        "bedrooms": 3,
        "sq_ft": 1000,
        "age": 1
    }
    response = client.post("/predict", json=payload)


    assert response.status_code == 200


    data = response.json()
    assert "predicted_price" in data
    assert data["currency"] == "USD"