from fastapi.testclient import TestClient
from main import app

# Create a test client that simulates API requests
client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "API is running!"}


def test_predict_price():
    # The exact same payload you just tested manually
    payload = {
        "bedrooms": 3,
        "sq_ft": 1000,
        "age": 1
    }
    response = client.post("/predict", json=payload)

    # Check if the API responds successfully
    assert response.status_code == 200

    # Check if the response contains our expected keys
    data = response.json()
    assert "predicted_price" in data
    assert data["currency"] == "USD"