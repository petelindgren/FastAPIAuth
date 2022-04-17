from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "PDM docker-compose version of SingleFile Hello World"}
