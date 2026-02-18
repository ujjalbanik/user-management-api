from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.user_repository import (
    get_user_by_email,
    create_user,
    get_user_by_id,
    update_user,
    delete_user
)
from app.core.security import (
    hash_password, 
    verify_password, 
    create_access_token
)


def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed = hash_password(password)
    return create_user(db, email, hashed)


def login_user(db, email: str, password: str):
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}


def update_user_profile(db, current_user, user_id: int, email, password):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Ownership rule
    if current_user.id != user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not allowed")

    hashed = hash_password(password) if password else None

    return update_user(db, user, email, hashed)


def delete_user_profile(db, current_user, user_id: int):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if current_user.id != user.id and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not allowed")

    delete_user(db, user)
    return {"message": "User deleted successfully"}