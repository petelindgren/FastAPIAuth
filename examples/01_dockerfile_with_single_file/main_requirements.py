from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Requirements Dockerfile version of SingleFile Hello World"}
