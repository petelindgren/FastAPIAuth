# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5


class Settings:
    PROJECT_NAME: str = "Fast API Authentication"
    PROJECT_VERSION: str = "1.0.0"


settings = Settings()
