from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_send_data():
    response = client.post(
        "/send_reviews",
        headers={"X-Token": "coneofsilence"},
        json={"text": "My car is a BMW, and it is made in Germany."},
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }
