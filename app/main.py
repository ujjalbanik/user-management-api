from fastapi import FastAPI
from app.db.database import engine, Base
from app.models import user
from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router
from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException
from app.core.response import error_response


app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "API is running properly 🚀"}

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(exc.detail),
    )
