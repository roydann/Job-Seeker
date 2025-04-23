from pydantic import BaseModel

class JobSearchRequest(BaseModel):
    job_title: str
    level: str
    country: str