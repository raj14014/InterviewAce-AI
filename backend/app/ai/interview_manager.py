from app.ai.llm_interviewer import LLMInterviewer
from app.ai.answer_evaluator import AnswerEvaluator
from app.ai.speech_to_text import SpeechToText
from app.ai.voice_analyzer import VoiceAnalyzer
from app.database.interview_history import InterviewHistory


class InterviewManager:

    def __init__(self):

        self.llm = LLMInterviewer()

        self.evaluator = AnswerEvaluator()

        self.stt = SpeechToText()

        self.voice = VoiceAnalyzer()

        self.database = InterviewHistory()

    def start_interview(self):

        return self.llm.generate_question()

    def process_audio(
        self,
        audio_path,
        duration,
        question,
    ):

        # Speech → Text
        answer = self.stt.transcribe(audio_path)

        # AI Evaluation
        evaluation = self.evaluator.evaluate(
            question,
            answer,
        )

        # Voice Analysis
        voice = self.voice.analyze(
            answer,
            duration,
        )

        # Overall Score
        overall_score = voice["confidence_score"]

        # Next Adaptive Question
        next_question = self.llm.next_question(
            question,
            answer,
            overall_score,
        )

        result = {
            "question": question,
            "answer": answer,
            "evaluation": evaluation,
            "voice": voice,
            "overall_score": voice["confidence_score"],
            "next_question": next_question,
            "placement_ready": (
                "Yes"
                if voice["confidence_score"] >= 75
                else "No"
            ),
        }

        # Save Interview
        self.database.save(
            question,
            answer,
            result,
        )

        return result