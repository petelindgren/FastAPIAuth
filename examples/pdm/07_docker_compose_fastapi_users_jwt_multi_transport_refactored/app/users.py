from typing import Optional

from app.db import get_user_db
from app.models import User, UserCreate, UserDB, UserUpdate
from app.settings import SECRET_KEY
from app.strategies import get_jwt_strategy
from app.transports import bearer_transport, cookie_transport
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend
from fastapi_users.db import SQLAlchemyUserDatabase


class UserManager(BaseUserManager[UserCreate, UserDB]):
    user_db_model = UserDB

    reset_password_token_secret = SECRET_KEY
    verification_token_secret = SECRET_KEY

    async def on_after_register(self, user: UserDB, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: UserDB, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: UserDB, token: str, request: Optional[Request] = None
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
    get_strategy=get_jwt_strategy,
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
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_active_user = fast_api_users.current_user(
    active=True, get_enabled_backends=get_enabled_backends
)
