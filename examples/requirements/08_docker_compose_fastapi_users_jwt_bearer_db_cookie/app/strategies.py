from typing import List

from app.core.settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY
from app.db.base import get_access_token_db
from app.db.schemas import UserCreate, UserDB
from app.db.schemas.auth import AccessToken
from fastapi import Depends
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)


class Session:
    pass


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=SECRET_KEY,
        algorithm=ALGORITHM,
        lifetime_seconds=60 * ACCESS_TOKEN_EXPIRE_MINUTES,
    )


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy[UserCreate, UserDB, AccessToken]:
    return DatabaseStrategy(
        access_token_db, lifetime_seconds=60 * ACCESS_TOKEN_EXPIRE_MINUTES
    )
