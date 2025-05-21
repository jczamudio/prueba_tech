from fastapi import FastAPI
from app.api.routes import router
import uvicorn

app = FastAPI()
app.include_router(router)

print("Starting FastAPI application...")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000)
