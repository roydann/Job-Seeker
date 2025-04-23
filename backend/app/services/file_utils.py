import os
from fastapi import UploadFile

UPLOAD_DIR = "uploaded_resumes"

def save_resume_file(file: UploadFile, user_id: str) -> str:
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    filename = f"{user_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        content = file.file.read()
        f.write(content)

    return file_path