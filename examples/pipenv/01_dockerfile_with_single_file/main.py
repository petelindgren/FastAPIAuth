from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Dockerfile version of SingleFile Hello World"}
