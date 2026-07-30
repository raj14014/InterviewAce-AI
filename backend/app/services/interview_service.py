from app.ai.llm_interviewer import LLMInterviewer
from app.ai.answer_evaluator import AnswerEvaluator
from app.database.interview_history import InterviewHistory


class InterviewService:

    def __init__(self):

        self.interviewer = LLMInterviewer()

        self.evaluator = AnswerEvaluator()

        self.database = InterviewHistory()

    def process_answer(
        self,
        question,
        answer,
    ):
        """
        Evaluate answer and save interview history.
        """

        evaluation = self.evaluator.evaluate(
            question,
            answer,
        )

        self.database.save(
            question,
            answer,
            evaluation,
        )

        return evaluation

    def next_question(self):

        return self.interviewer.generate_question()