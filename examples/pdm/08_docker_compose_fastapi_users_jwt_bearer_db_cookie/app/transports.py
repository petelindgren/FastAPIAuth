from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi_users.authentication import BearerTransport, CookieTransport

# https://fastapi-users.github.io/fastapi-users/usage/current-user/#dynamically-enable-authentication-backends
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
cookie_transport = CookieTransport(cookie_max_age=60 * ACCESS_TOKEN_EXPIRE_MINUTES)
