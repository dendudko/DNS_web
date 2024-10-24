from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import get_settings

settings = get_settings()

DATABASE_URL = (f"postgresql+asyncpg://{settings.db_username}:{settings.db_password}"
                f"@{settings.db_host}:{settings.db_port}/{settings.db_database}")
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session
