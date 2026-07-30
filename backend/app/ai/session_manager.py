from app.services.interview_service import InterviewService


class InterviewSession:

    def __init__(self):

        self.service = InterviewService()

        self.current_question = None

        self.finished = False

    def start(self):

        self.current_question = self.service.next_question()

        return self.current_question

    def answer(self, answer):

        evaluation = self.service.process_answer(
            self.current_question,
            answer,
        )

        self.current_question = self.service.next_question()

        return {
            "evaluation": evaluation,
            "next_question": self.current_question,
        }