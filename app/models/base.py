from sqlmodel import SQLModel, Field


# Абстрактный базовый класс
class Base(SQLModel):
    id: int = Field(default=None, primary_key=True)
    __abstract__ = True  # Этот класс не будет превращен в таблицу

    def get_primary_key(self):
        return self.id
    # Generate __tablename__ automatically
    # @classmethod
    # @property
    # def __tablename__(cls) -> str:
    #     return cls.__name__.lower()
