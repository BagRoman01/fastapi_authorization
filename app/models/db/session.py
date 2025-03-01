from sqlmodel import Field
from app.models.base import Base
from app.models.schemas.session import SessionCreate


class Session(Base, SessionCreate):
    id: int = Field(default=None, primary_key=True)

    def get_primary_key(self):
        return self.id
