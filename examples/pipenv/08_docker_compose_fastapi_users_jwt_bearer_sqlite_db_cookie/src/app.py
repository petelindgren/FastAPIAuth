from fastapi import FastAPI
from src import settings
from src.urls import url_router


def include_router(router_app):
    router_app.include_router(url_router)


def start_application():
    fast_app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(fast_app)
    return fast_app


app = start_application()


@app.get("/")
def root_api():
    return {"root": "Analog Interface"}
