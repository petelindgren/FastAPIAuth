import uvicorn

if __name__ == "__main__":
    uvicorn.run("fast_api_oauth2:app", host="0.0.0.0", log_level="info")
