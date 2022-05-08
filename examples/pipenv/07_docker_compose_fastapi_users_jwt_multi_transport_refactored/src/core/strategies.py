from fastapi_users.authentication import JWTStrategy
from src.settings import ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM, SECRET_KEY


class Session:
    pass


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=SECRET_KEY,
        algorithm=ALGORITHM,
        lifetime_seconds=60 * ACCESS_TOKEN_EXPIRE_MINUTES,
    )
