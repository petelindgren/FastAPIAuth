# to get a string like this run:
# openssl rand -hex 32
PROJECT_NAME: str = "Fast API Authentication"
PROJECT_VERSION: str = "1.0.0"

SECRET_KEY: str = "MyV0iceIsMyPassp0rt"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 5
DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
