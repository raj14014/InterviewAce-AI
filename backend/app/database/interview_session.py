import uuid


class InterviewSession:

    def __init__(self):

        self.sessions = {}

    def create_session(self, questions):

        session_id = str(uuid.uuid4())

        self.sessions[session_id] = {

            "questions": questions,

            "index": 0,

            "answers": [],

            "scores": [],

        }

        return session_id

    def get_question(self, session_id):

        session = self.sessions[session_id]

        if session["index"] >= len(session["questions"]):

            return "Interview Finished."

        question = session["questions"][session["index"]]

        session["index"] += 1

        return question

    def save_answer(
        self,
        session_id,
        answer,
        score,
    ):

        self.sessions[session_id]["answers"].append(answer)

        self.sessions[session_id]["scores"].append(score)

    def get_session(self, session_id):

        return self.sessions.get(session_id)