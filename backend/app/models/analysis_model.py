from pydantic import BaseModel
from typing import List, Optional


class EmotionResult(BaseModel):
    emotion: str
    confidence: float


class EyeContactResult(BaseModel):
    eye_contact_score: float


class SpeechResult(BaseModel):
    speech_text: Optional[str] = None
    confidence_score: float


class AnalysisResult(BaseModel):
    overall_score: float
    emotions: List[EmotionResult]
    eye_contact: EyeContactResult
    speech: SpeechResult
    feedback: List[str]