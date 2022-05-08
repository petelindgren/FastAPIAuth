import os

from fastapi import FastAPI

app = FastAPI()

package_manager = os.getenv(
    "PACKAGE_MANAGER_NAME", "needs 'environment' in 'docker-compose' file"
)


@app.get("/")
async def root():
    return {"root": f"Analog Interface ({package_manager})"}
