from fastapi import FastAPI
from app.api import upload, job_search

app = FastAPI()

app.include_router(upload.router)
app.include_router(job_search.router)

@app.get("/")
def read_root():
    return {"message": "Backend is running!"}