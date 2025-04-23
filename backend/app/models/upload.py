from pydantic import BaseModel
from enum import Enum

class ExperienceLevel(str, Enum):
    student = "Student"
    Junior = "Junior"
    mid = "Mid"
    senior = "Senior"

class UploadMetadata(BaseModel):
    job_title: str
    country: str
    level: ExperienceLevel