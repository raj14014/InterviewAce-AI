from fastapi import APIRouter, UploadFile, File

import shutil
import os

from app.ai.resume_parser import ResumeParser
from app.ai.resume_question_generator import ResumeQuestionGenerator
from app.ai.interview_manager import InterviewManager

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)

parser = ResumeParser()

generator = ResumeQuestionGenerator()

manager = InterviewManager()


@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    pdf_path = f"uploads/{file.filename}"

    with open(pdf_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    text = parser.extract_text(pdf_path)

    resume = parser.parse_resume(text)

    questions = generator.generate(resume)

    manager.llm.load_questions(questions)

    return {

        "resume": resume,

        "questions": questions,

    }