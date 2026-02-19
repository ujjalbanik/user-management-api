from app.models.user import User
from tests.conftest import client
from app.db.database import SessionLocal

def create_and_login(email, password="password123"):
    client.post("/users/", json={"email": email, "password": password})
    res = client.post("/auth/login", json={"email": email, "password": password})
    token = res.json()["access_token"]
    return token


def test_normal_user_cannot_view_all_users():
    token = create_and_login("normal@example.com")

    response = client.get(
        "/users/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 403


def test_admin_can_view_all_users(db_session):
    email = "admin@example.com"
    password = "password123"

    # create user via API
    client.post("/users/", json={"email": email, "password": password})

    # promote using SAME test DB session
    user = db_session.query(User).filter(User.email == email).first()
    user.is_admin = True
    db_session.commit()

    # login
    res = client.post("/auth/login", json={"email": email, "password": password})
    token = res.json()["access_token"]

    response = client.get(
        "/users/",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
