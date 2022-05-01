from app.db import Base
from fastapi_users import models
from fastapi_users.authentication.strategy.db import BaseAccessToken
from fastapi_users.db import SQLAlchemyBaseUserTable
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable


class User(models.BaseUser):
    pass


class UserCreate(models.BaseUserCreate):
    pass


class UserUpdate(models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass


class AccessToken(BaseAccessToken):
    pass


class AccessTokenTable(SQLAlchemyBaseAccessTokenTable, Base):
    pass
