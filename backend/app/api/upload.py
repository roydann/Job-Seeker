from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.models.upload import ExperienceLevel
from app.services.file_utils import save_resume_file
import uuid

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(
    resume: UploadFile = File(...),
    job_title: str = Form(...),
    country: str = Form(...),
    level: ExperienceLevel = Form(...),
):
    if resume.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF resumes are supported.")
    
    user_id = str(uuid.uuid4())
    saved_path = save_resume_file(resume, user_id)
    
    return {
        "message": "Resume uploaded successfully!",
        "file_path": saved_path,
        "user_preferences": {
            "job_title": job_title,
            "country": country,
            "level": level
        }
    }