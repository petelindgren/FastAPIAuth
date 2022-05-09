# https://www.fastapitutorial.com/blog/database-connection-fastapi/
from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.auth.models import AccessTokenTable, User
from src.core.storage.base_classes import Base
from src.core.storage.sessions import async_session_maker, engine, get_db_session


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_db_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_token_db(session: AsyncSession = Depends(get_db_session)):
    yield SQLAlchemyAccessTokenDatabase(session, AccessTokenTable)
