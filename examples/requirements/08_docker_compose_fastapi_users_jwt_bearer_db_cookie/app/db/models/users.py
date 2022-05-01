from app.db.base_classes import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable


class UserTable(Base, SQLAlchemyBaseUserTable):
    pass
