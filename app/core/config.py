import secrets
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, ValidationError


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=['../../.env', '../.env', '.env'],
        env_file_encoding='utf-8',
        extra='ignore',
        case_sensitive=True,
    )

    # DATABASE GROUP
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_USER: str
    DATABASE_PASS: str
    DATABASE_NAME: str

    # AUTHENTICATION GROUP
    AUTH_SECRET_KEY: str
    AUTH_ALGORITHM: str
    AUTH_ACCESS_TOKEN_EXPIRE_MINUTES: int
    AUTH_REFRESH_TOKEN_EXPIRE_MINUTES: int

    # FRONTEND GROUP
    FRONTEND_BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    # DEPLOYMENT GROUP
    DEPLOY_HOST: str
    DEPLOY_PORT: int

    # Additional fields
    MODE: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DATABASE_USER}:{self.DATABASE_PASS}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"

    def generate_secret_key(self) -> None:
        """Generate a secret key if not provided."""
        self.AUTH_SECRET_KEY = secrets.token_urlsafe(32)

    def __init__(self):
        super().__init__()
        # Generate secret key if it is not provided
        if not self.AUTH_SECRET_KEY:
            self.generate_secret_key()


try:
    settings = Settings()
except ValidationError as e:
    print(f"Validation error: {e}")
