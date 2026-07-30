"""
InterviewAce AI
Speech Tracker
"""


class SpeechTracker:

    def __init__(self):

        self.total_words = 0
        self.total_fillers = 0
        self.average_wpm = 0

    # -------------------------
    # Update Speech Statistics
    # -------------------------

    def update(
        self,
        wpm,
        fillers,
        text,
    ):

        self.average_wpm = wpm
        self.total_fillers = fillers
        self.total_words = len(text.split())

    # -------------------------
    # Communication Score
    # -------------------------

    def communication_score(self):

        score = 100

        if self.average_wpm < 80:
            score -= 10

        elif self.average_wpm > 170:
            score -= 10

        if self.total_fillers > 8:
            score -= 15

        elif self.total_fillers > 4:
            score -= 8

        return max(score, 0)

    # -------------------------
    # Feedback
    # -------------------------

    def feedback(self):

        feedback = []

        if self.average_wpm < 80:
            feedback.append("Speak slightly faster.")

        elif self.average_wpm > 170:
            feedback.append("Speak a little slower.")

        else:
            feedback.append("Speaking speed is good.")

        if self.total_fillers <= 3:
            feedback.append("Very few filler words.")

        else:
            feedback.append("Reduce filler words like 'um' and 'uh'.")

        return feedback