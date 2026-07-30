class LLMInterviewer:

    def __init__(self):

        self.questions = []

        self.index = 0

    def load_questions(self, questions):

        self.questions = questions

        self.index = 0

    def generate_question(self):

        if self.index >= len(self.questions):

            return "Interview Finished."

        question = self.questions[self.index]

        self.index += 1

        return question

    def next_question(
        self,
        previous_question,
        candidate_answer,
        score=70,
    ):

        if score >= 90:

            return self.generate_question()

        elif score >= 70:

            return self.generate_question()

        else:

            return (
                "Can you explain your previous answer in more detail?"
            )