import pytest
from app.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello DevOps World!" in response.data


def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}