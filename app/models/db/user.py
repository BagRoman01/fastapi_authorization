from pydantic import EmailStr
from sqlmodel import Field
from app.models.base import Base


class User(Base):
    id: int = Field(default=None, primary_key=True)
    hashed_password: str = Field(nullable=False)
    age: int = Field(default=None, nullable=True)
    email: EmailStr = Field(nullable=False)

    def get_primary_key(self):
        return self.id
