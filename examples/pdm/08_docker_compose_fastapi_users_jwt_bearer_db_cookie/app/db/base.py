# https://www.fastapitutorial.com/blog/database-connection-fastapi/
from typing import AsyncGenerator

from app.db.base_classes import Base
from app.db.models import AccessTokenTable, UserTable
from app.db.schemas import AccessToken, UserDB
from app.db.sessions import async_db_engine, get_db_session
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from sqlalchemy.ext.asyncio import AsyncSession


async def create_db_and_tables():
    async with async_db_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_db_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(UserDB, session, UserTable)


async def get_access_token_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyAccessTokenDatabase(AccessToken, session, AccessTokenTable)
