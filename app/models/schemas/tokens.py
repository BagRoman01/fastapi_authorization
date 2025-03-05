from sqlmodel import SQLModel, Field


class Tokens(SQLModel, table=False):
    access_token: str | None = Field(default=None, nullable=True)
    refresh_token: str | None = Field(default=None, nullable=True)
