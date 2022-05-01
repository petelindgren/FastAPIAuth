from app.core.settings import settings
from app.urls import url_router
from fastapi import FastAPI


def include_router(app):
    app.include_router(url_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_application()


@app.get("/")
def hello_api():
    return {"msg": "Hello API"}
