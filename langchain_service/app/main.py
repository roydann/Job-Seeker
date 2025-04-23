from fastapi import FastAPI, Request
from app.agents.job_finder_agent import job_agent

app = FastAPI()

@app.post("/find-jobs")
async def find_jobs(request: Request):
    data = await request.json()
    query = data.get("query")
    if not query:
        return {"error": "Query field is required."}
    
    result = job_agent.run(query)
    return{"results": result}