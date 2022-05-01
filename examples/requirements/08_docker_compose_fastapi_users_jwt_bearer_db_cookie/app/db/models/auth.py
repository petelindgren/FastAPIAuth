from app.db.base_classes import Base
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable


class AccessTokenTable(SQLAlchemyBaseAccessTokenTable, Base):
    pass
