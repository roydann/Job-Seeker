from fastapi import APIRouter, HTTPException
from app.models.job_search import JobSearchRequest
import httpx
import os

router = APIRouter()

LANGCHAIN_URL = os.getenv("LANGCHAIN_API_URL", "http://langchain:9000")

@router.post("/search-jobs")
async def search_jobs(query: JobSearchRequest):
    formatted_query = f"{query.level} {query.job_title} jobs in {query.country}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{LANGCHAIN_URL}/find-jobs",
                json={"query": formatted_query},
                timeout=30
            )

        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))