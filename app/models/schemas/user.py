from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel, Field
from app.exceptions.auth_exceptions import ShortPasswordError


class UserLogin(SQLModel, table=False):
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)

    @field_validator('password')
    def password_length(self, value):
        if len(value) < 6:
            raise ShortPasswordError
        return value


class UserCreate(SQLModel, UserLogin):
    age: int = Field(default=None, nullable=True)







