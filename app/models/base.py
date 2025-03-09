from sqlmodel import SQLModel, Field


# Абстрактный базовый класс
class Base(SQLModel):
    id: int = Field(default=None, primary_key=True)
    __abstract__ = True  # Этот класс не будет превращен в таблицу

    @staticmethod
    def get_primary_key(model):
        """Метод возвращает primary_key для модели"""
        return model.id  # Возвращаем id как поле primary_key для переданной модели

    # # Generate __tablename__ automatically
    # @classmethod
    # def __tablename__(cls) -> str:
    #     return cls.__name__.lower()
