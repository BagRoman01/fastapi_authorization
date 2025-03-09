from sqlmodel import SQLModel, Field


class ExchangeCurrency(SQLModel, table=False):
    base_cur: str | None = Field(default=None, nullable=True)
    cur_to: str | None = Field(default=None, nullable=True)
    amount: float = 1


class HistoryExchangeCurrency(ExchangeCurrency):
    date: str | None = Field(default=None, nullable=True)

