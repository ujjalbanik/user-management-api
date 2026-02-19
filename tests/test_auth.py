from tests.conftest import client
import uuid

def random_email():
    return f"{uuid.uuid4()}@test.com"

def test_user_registration():
    response = client.post(
        "/users/",
        json={"email": random_email(), "password": "password123"}
    )

    assert response.status_code == 201
    data = response.json()
    assert data["success"] is True


def test_user_login():
    email = random_email()
    client.post(
        "/users/",
        json={"email": email, "password": "password123"}
    )

    response = client.post(
        "/auth/login",
        json={"email": email, "password": "password123"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()


def test_get_current_user():
    email = random_email()
    client.post(
        "/users/",
        json={"email": email, "password": "password123"}
    )

    login = client.post(
        "/auth/login",
        json={"email": email, "password": "password123"}
    )

    token = login.json()["access_token"]

    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
