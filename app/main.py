from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user
from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "API is running properly 🚀"}

