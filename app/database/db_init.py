from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings


engine = create_async_engine(settings.ASYNC_DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)



