from app.db.base_classes import Base
from fastapi_users.authentication.strategy.db import BaseAccessToken
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable


class AccessToken(BaseAccessToken):
    pass


class AccessTokenTable(SQLAlchemyBaseAccessTokenTable, Base):
    pass
