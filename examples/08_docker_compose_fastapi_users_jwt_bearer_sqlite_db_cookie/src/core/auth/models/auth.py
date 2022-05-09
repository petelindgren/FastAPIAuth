from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTableUUID
from src.core.storage.base_classes import Base


class AccessTokenTable(SQLAlchemyBaseAccessTokenTableUUID, Base):
    """

    Notes
    -----
    * MRO matters https://www.python.org/download/releases/2.3/mro/
    * When using multi-inheritance the Declarative `Base` must be
      the class on the far right or the app will not start because
      of an error message like this::

        sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column
        'accesstoken.user_id' could not find table 'user' with which to generate
        a foreign key to target column 'id'

    """

    pass
