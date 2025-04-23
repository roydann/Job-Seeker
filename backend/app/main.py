from fastapi import FastAPI
from app.api import upload

app = FastAPI()

app.include_router(upload.router)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}