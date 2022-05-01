from app.db.base_classes import Base
from fastapi_users import models
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable


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
