# https://fastapi.tiangolo.com/deployment/docker/#create-the-fastapi-code
import os
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


package_manager = os.getenv(
    "PACKAGE_MANAGER_NAME", "needs 'environment' in 'docker-compose' file"
)


@app.get("/")
async def root():
    return {"root": f"Analog Interface ({package_manager})"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
