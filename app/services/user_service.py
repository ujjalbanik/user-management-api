from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repo import get_user_by_email, create_user
from app.core.security import hash_password


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed = hash_password(password)
    return create_user(db, email, hashed)
