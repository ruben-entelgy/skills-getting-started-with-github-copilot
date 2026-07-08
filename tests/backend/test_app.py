from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_delete_participant_unregisters_student():
    response = client.delete("/activities/Chess Club/participants/michael@mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in response.json()["participants"]


def test_delete_participant_returns_404_for_unknown_student():
    response = client.delete("/activities/Chess Club/participants/unknown@mergington.edu")

    assert response.status_code == 404


def test_signup_returns_success_message():
    response = client.post("/activities/Chess Club/signup?email=signup-test@mergington.edu")

    assert response.status_code == 200
    assert "Signed up signup-test@mergington.edu" in response.json()["message"]
