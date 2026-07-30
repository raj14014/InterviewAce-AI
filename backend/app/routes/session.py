from fastapi import APIRouter

from app.ai.interview_manager import InterviewManager

router = APIRouter(
    prefix="/session",
    tags=["Interview Session"],
)

manager = InterviewManager()


@router.post("/start")
def start_session():

    question = manager.start_interview()

    return {
        "message": "Interview Session Started",
        "question": question,
    }


@router.post("/answer")
def answer(question: str, duration: int, audio_path: str):

    result = manager.process_audio(
        audio_path,
        duration,
        question,
    )

    return result