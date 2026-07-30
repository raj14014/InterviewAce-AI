from pydantic import BaseModel
from typing import Optional


class ResumeResponse(BaseModel):
    filename: str
    file_url: str
    message: str


class ResumeInfo(BaseModel):
    filename: str
    upload_date: Optional[str] = None