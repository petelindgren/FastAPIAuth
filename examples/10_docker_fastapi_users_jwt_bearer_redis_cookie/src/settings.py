import os

# to get a string like this run:
# openssl rand -hex 32
PROJECT_NAME: str = "Fast API Authentication"
PROJECT_VERSION: str = "1.0.0"

SECRET_KEY: str = "MyV0iceIsMyPassp0rt"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 5
DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
REDIS_URL: str = os.environ.get("REDIS_URL", "redis://localhost:6379")
