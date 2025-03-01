from sqlmodel import Field
from app.models.base import Base
from app.models.schemas.session import SessionCreate


class Session(Base, SessionCreate, table=True):
    pass

