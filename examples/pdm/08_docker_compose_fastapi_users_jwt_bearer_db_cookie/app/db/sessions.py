# https://www.fastapitutorial.com/blog/database-connection-fastapi/
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# from core.config import settings


# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# if you don't want to install postgres or any database, use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# https://docs.sqlalchemy.org/en/14/core/engines.html#engine-creation-api
# db_engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# session_maker = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

# https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#engine-api-documentation
db_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
async_session_maker = sessionmaker(
    db_engine, class_=AsyncSession, expire_on_commit=False
)
