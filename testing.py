from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_send_data():
    response = client.post(
        "/send_reviews",
        # headers={"X-Token": "coneofsilence"},
        json={"text": "My car is a BMW, and it is made in Germany."},
    )
    assert response.status_code == 422
    assert response.json() == {
        [
            {"entity": "BMW", "entity_label": "ORG"},
            {"entity": "Germany", "entity_label": "GPE"},
        ]
    }
