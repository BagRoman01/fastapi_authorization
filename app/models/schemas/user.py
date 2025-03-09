from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel, Field
from app.exceptions.auth_exceptions import ShortPasswordError


class UserLogin(SQLModel, table=False):
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)

    @field_validator('password')
    @classmethod
    def password_length(cls, value):
        if len(value) < 6:
            raise ShortPasswordError("Пароль должен содержать не менее 6 символов.")
        return value


# Модель для регистрации пользователя
class UserCreate(SQLModel, table=False):
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)
    age: int = Field(default=None, nullable=True)

    # Валидация длины пароля
    @field_validator('password')
    @classmethod
    def password_length(cls, value):
        if len(value) < 6:
            raise ShortPasswordError("Пароль должен содержать не менее 6 символов.")
        return value







