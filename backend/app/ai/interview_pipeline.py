from app.ai.question_generator import QuestionGenerator
from app.ai.speech_to_text import SpeechToText
from app.ai.voice_analyzer import VoiceAnalyzer
from app.ai.answer_evaluator import AnswerEvaluator
from app.database.interview_history import InterviewHistory

from app.ai.face_detector import FaceDetector
from app.ai.emotion_detector import EmotionDetector
from app.ai.eye_contact import EyeContactDetector
from app.ai.head_pose import HeadPoseEstimator

class InterviewPipeline:

    def __init__(self):

        self.question_generator = QuestionGenerator()

        self.speech_to_text = SpeechToText()

        self.voice_analyzer = VoiceAnalyzer()

        self.answer_evaluator = AnswerEvaluator()

        self.database = InterviewHistory()
        
        self.face_detector = FaceDetector()
        
        self.emotion_detector = EmotionDetector()
        
        self.eye_contact = EyeContactDetector()

        self.head_pose = HeadPoseEstimator()

    def generate_question(self):
        """
        Generate a new interview question.
        """
        return self.question_generator.generate()

    def process_audio(
        self,
        audio_path,
        duration
    ):
        """
        Convert speech into text.
        """
        answer = self.speech_to_text.transcribe(audio_path)

        voice_result = self.voice_analyzer.analyze(
            answer,
            duration
        )

        return answer, voice_result
    
    def process_video(self, frame):

        face = self.face_detector.detect(frame)

        emotion = self.emotion_detector.detect(frame)

        eye = self.eye_contact.detect(frame)

        pose = self.head_pose.detect(frame)

        return {
            "face": face,
            "emotion": emotion,
            "eye_contact": eye,
            "head_pose": pose
        }

    def evaluate(
        self,
        question,
        answer,
    ):
        """
        Evaluate candidate answer.
        """
        result = self.answer_evaluator.evaluate(
            question,
            answer
        )

        self.database.save(
            question,
            answer,
            result
        )

        return result

    def complete_interview(
        self,
        question,
        audio_path,
        duration,
        frame=None
    ):

        answer, voice = self.process_audio(
            audio_path,
            duration
        )

        evaluation = self.evaluate(
            question,
            answer
        )
        
        visual = None

        if frame is not None:
            visual = self.process_video(frame)

        return {
            "question": question,
            "answer": answer,
            "voice": voice,
            "visual": visual,
            "evaluation": evaluation
        }