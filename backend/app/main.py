from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.routes.analysis import router as analysis_router
from app.routes.session import router as session_router
from app.routes.resume import router as resume_router
from app.routes.history import router as history_router

app = FastAPI(
    title="InterviewAce AI Backend",
    version="2.0.0",
    description="AI Powered Interview Analyzer"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routes
app.include_router(analysis_router)
app.include_router(session_router)
app.include_router(resume_router)
app.include_router(history_router)


@app.get("/")
def root():
    return {
        "message": "InterviewAce AI Backend Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }