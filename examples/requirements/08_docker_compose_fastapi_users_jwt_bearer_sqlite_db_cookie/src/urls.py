from fastapi import APIRouter, Depends
from src.core.auth.models import User
from src.core.auth.schemas.users import UserCreate, UserRead, UserUpdate
from src.core.storage.base import create_db_and_tables
from src.users import (
    bearer_backend,
    cookie_backend,
    current_active_user,
    fast_api_users,
)

url_router = APIRouter()


url_router.include_router(
    fast_api_users.get_auth_router(bearer_backend), prefix="/auth/jwt", tags=["auth"]
)
url_router.include_router(
    fast_api_users.get_auth_router(cookie_backend), prefix="/auth/cookie", tags=["auth"]
)
url_router.include_router(
    fast_api_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
url_router.include_router(
    fast_api_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
url_router.include_router(
    fast_api_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
url_router.include_router(
    fast_api_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@url_router.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@url_router.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return (
        f"Hello, {user.email}. You are authenticated using JWT Strategy transported by Bearer"
        f" or DB Strategy transported by Cookie."
    )


@url_router.get("/protected-route-only-jwt")
def protected_route_only_jwt(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated using JWT Strategy transported by Bearer."


@url_router.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
