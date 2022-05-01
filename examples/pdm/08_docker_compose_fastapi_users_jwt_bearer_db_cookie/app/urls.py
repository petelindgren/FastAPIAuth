from app.db.models.users import User, UserDB
from app.users import (
    bearer_backend,
    cookie_backend,
    current_active_user,
    fast_api_users,
)
from fastapi import APIRouter, Depends

url_router = APIRouter()

url_router.include_router(
    fast_api_users.get_auth_router(bearer_backend), prefix="/auth/jwt", tags=["auth"]
)
url_router.include_router(
    fast_api_users.get_auth_router(cookie_backend), prefix="/auth/cookie", tags=["auth"]
)
url_router.include_router(
    fast_api_users.get_register_router(), prefix="/auth", tags=["auth"]
)
url_router.include_router(
    fast_api_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
url_router.include_router(
    fast_api_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
url_router.include_router(
    fast_api_users.get_users_router(), prefix="/users", tags=["users"]
)


@url_router.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@url_router.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated using JWT Strategy transported by Cookie or Bearer."


@url_router.get("/protected-route-only-jwt")
def protected_route_only_jwt(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated using JWT Strategy transported by Bearer."
