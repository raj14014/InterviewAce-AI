from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from app.ai.interview_manager import InterviewManager

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

manager = InterviewManager()
question = manager.start_interview()


@router.get("/question")
def generate_question():

    question = manager.start_interview()

    return {
        "question": question
    }


@router.post("/answer")
async def analyze_answer(
    question: str = Form(...),
    duration: int = Form(...),
    audio: UploadFile = File(...)
):

    os.makedirs("temp", exist_ok=True)

    audio_path = f"temp/{audio.filename}"

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    result = manager.process_audio(
        audio_path,
        duration,
        question,
    )

    os.remove(audio_path)

    return result