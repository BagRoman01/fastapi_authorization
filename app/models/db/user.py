from pydantic import EmailStr
from sqlmodel import Field
from app.models.base import Base


class User(Base, table=True):
    hashed_password: str = Field(nullable=False)
    age: int | None = Field(default=None, nullable=True)
    email: EmailStr = Field(nullable=False)
