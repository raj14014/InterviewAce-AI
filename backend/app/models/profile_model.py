from pydantic import BaseModel
from typing import Optional


class ProfileCreate(BaseModel):
    full_name: str
    phone: str
    college: str
    degree: str
    branch: str
    graduation_year: int
    skills: list[str]
    linkedin: Optional[str] = None
    github: Optional[str] = None
    portfolio: Optional[str] = None


class ProfileResponse(ProfileCreate):
    id: str
    email: str