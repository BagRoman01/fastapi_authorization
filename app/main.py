from app.core.config import Settings  # Импортируйте класс Settings

# Создайте экземпляр класса
settings = Settings()

# Теперь вы можете использовать settings
print(settings.DATABASE_HOST)
print(settings.DATABASE_USER)
print(settings.FRONTEND_BACKEND_CORS_ORIGINS)
