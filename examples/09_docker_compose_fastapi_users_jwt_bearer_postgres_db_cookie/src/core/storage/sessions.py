# https://www.fastapitutorial.com/blog/database-connection-fastapi/
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.settings import DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True)
# expire_on_commit=False will prevent attributes from being expired after commit.
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# https://www.fastapitutorial.com/blog/dependencies-in-fastapi/
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
