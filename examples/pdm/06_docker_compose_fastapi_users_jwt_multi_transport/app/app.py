from app.db import create_db_and_tables
from app.models import User, UserDB
from app.users import cookie_backend, current_active_user, fast_api_users, jwt_backend
from fastapi import Depends, FastAPI

app = FastAPI()

app.include_router(
    fast_api_users.get_auth_router(jwt_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fast_api_users.get_auth_router(cookie_backend), prefix="/auth/cookie", tags=["auth"]
)
app.include_router(fast_api_users.get_register_router(), prefix="/auth", tags=["auth"])
app.include_router(
    fast_api_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fast_api_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(fast_api_users.get_users_router(), prefix="/users", tags=["users"])


@app.get("/authenticated-route")
async def authenticated_route(user: UserDB = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated using JWT Strategy transported by Cookie or Bearer."


@app.get("/protected-route-only-jwt")
def protected_route_only_jwt(user: User = Depends(current_active_user)):
    return f"Hello, {user.email}. You are authenticated using JWT Strategy transported by Bearer."


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
