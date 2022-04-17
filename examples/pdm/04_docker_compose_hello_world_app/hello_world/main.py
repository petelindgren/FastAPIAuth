# https://fastapi.tiangolo.com/deployment/docker/#create-the-fastapi-code
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World from MultiFile PDM docker-compose"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
