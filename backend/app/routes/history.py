from fastapi import APIRouter

from app.database.interview_history import InterviewHistory

router = APIRouter(
    prefix="/history",
    tags=["History"],
)

database = InterviewHistory()


@router.get("/")
def interview_history():

    return database.get_all()