import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import AuthenticationBackend

# Imports "from fastapi_users.db" fail, use "from fastapi_users_db_sqlalchemy"
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from src.core.auth.models import User
from src.core.storage.base import get_user_db
from src.core.strategies import get_database_strategy, get_jwt_strategy
from src.core.transports import bearer_transport, cookie_transport
from src.settings import SECRET_KEY


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


# https://fastapi-users.github.io/fastapi-users/usage/current-user/#dynamically-enable-authentication-backends
bearer_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
cookie_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)


async def get_enabled_backends(request: Request):
    """Return the enabled dependencies following custom logic."""
    if request.url.path == "/protected-route-only-jwt":
        return [bearer_backend]
    else:
        return [cookie_backend, bearer_backend]


fast_api_users = FastAPIUsers(
    get_user_manager,
    [cookie_backend, bearer_backend],
)

current_active_user = fast_api_users.current_user(
    active=True, get_enabled_backends=get_enabled_backends
)
