from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import register_user, delete_user_profile, update_user_profile
from app.db.database import get_db
from app.core.dependencies import get_current_user, get_current_admin
from app.models.user import User
from typing import List, Optional
from app.core.response import success_response

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = register_user(db, user.email, user.password)
    return success_response(new_user, "User registered successfully")


@router.get("/me", response_model=UserResponse)
def read_current_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/", response_model=List[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin),
    email: Optional[str] = Query(None),
    is_admin: Optional[bool] = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(5, ge=1, le=50),
):
    query = db.query(User)

    if email:
        query = query.filter(User.email.contains(email))

    if is_admin is not None:
        query = query.filter(User.is_admin == is_admin)

    users = query.offset((page - 1) * size).limit(size).all()

    return users

@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_user_profile(db, current_user, user_id, data.email, data.password)


@router.delete("/{user_id}")
def delete_user_account(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_user_profile(db, current_user, user_id)