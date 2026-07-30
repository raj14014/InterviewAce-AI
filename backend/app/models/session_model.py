from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InterviewSessionCreate(BaseModel):
    interview_id: str


class InterviewSessionResponse(BaseModel):
    session_id: str
    interview_id: str
    status: str
    started_at: datetime
    ended_at: Optional[datetime] = None


class InterviewSessionUpdate(BaseModel):
    status: Optional[str] = None
    ended_at: Optional[datetime] = None