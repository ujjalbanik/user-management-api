from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest, Token
from app.services.user_service import login_user
from app.db.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, data.email, data.password)
