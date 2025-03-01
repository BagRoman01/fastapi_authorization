from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class SessionCreate(SQLModel, table=False):
    user_id: int = Field(foreign_key="user.id")
    refresh_token: str = Field(default=None, nullable=False)
    exp_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    fingerprint: str = Field(nullable=False)