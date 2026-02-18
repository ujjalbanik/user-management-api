from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    @classmethod
    def validate_password(cls, value: str):
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters")

        if len(value.encode("utf-8")) > 72:
            raise ValueError("Password too long (max 72 bytes)")

        return value


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None