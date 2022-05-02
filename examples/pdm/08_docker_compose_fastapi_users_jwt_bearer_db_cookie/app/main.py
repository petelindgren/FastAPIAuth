from app.core.settings import SQLALCHEMY_DATABASE_URL, settings
from app.db.base_classes import Base
from app.db.sessions import async_db_engine
from app.urls import url_router
from fastapi import FastAPI
from sqlalchemy import create_engine


def include_router(app):
    app.include_router(url_router)


def create_tables():
    """
    Create table non-async
    https://docs.sqlalchemy.org/en/14/_modules/examples/asyncio/async_orm.html
    """

    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"msg": "Hello API"}
