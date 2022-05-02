# https://www.fastapitutorial.com/blog/database-connection-fastapi/
from typing import AsyncGenerator

from app.core.settings import ASYNC_SQLALCHEMY_DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# if you don't want to install postgres or any database, use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine


# https://docs.sqlalchemy.org/en/14/core/engines.html#engine-creation-api
# db_engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# session_maker = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#engine-api-documentation
# https://docs.sqlalchemy.org/en/14/_modules/examples/asyncio/async_orm.html

async_db_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL, echo=True)
# expire_on_commit=False will prevent attributes from being expired after commit.
AsyncSessionLocal = sessionmaker(
    async_db_engine, expire_on_commit=False, class_=AsyncSession
)


# https://www.fastapitutorial.com/blog/dependencies-in-fastapi/
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
