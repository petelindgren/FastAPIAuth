from fastapi import Depends
from fastapi_users.authentication import JWTStrategy
from fastapi_users.authentication.strategy.db import (
    AccessTokenDatabase,
    DatabaseStrategy,
)
from src.core.auth.schemas import AccessToken
from src.core.storage.base import get_access_token_db
from src.settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


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
) -> DatabaseStrategy:
    """
    Reference:
    * https://fastapi-users.github.io/fastapi-users/10.0/configuration/authentication/strategies/database/?h=get_database_strategy#strategy
    """
    return DatabaseStrategy(
        access_token_db, lifetime_seconds=60 * ACCESS_TOKEN_EXPIRE_MINUTES
    )
