from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, Column, DateTime


class SessionCreate(SQLModel, table=False):
    user_id: int = Field(foreign_key="user.id")
    refresh_token: str = Field(default=None, nullable=False)
    exp_at: datetime = Field(sa_column=Column(DateTime(timezone=True)), default=None)
    created_at: datetime = Field(sa_column=Column(DateTime(timezone=True)), default=None)
    fingerprint: str = Field(nullable=False)

