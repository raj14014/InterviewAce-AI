"""
InterviewAce AI
Communication Analyzer
"""


class CommunicationAnalyzer:

    def __init__(self):
        pass

    def communication_score(self, wpm, fillers):

        score = 100

        # -------------------------
        # Speaking Speed
        # -------------------------

        if wpm < 80:
            score -= 15

        elif wpm > 160:
            score -= 15

        elif 100 <= wpm <= 140:
            score += 5

        # -------------------------
        # Fillers
        # -------------------------

        score -= fillers * 3

        score = max(0, min(100, score))

        return round(score, 1)

    def feedback(self, wpm, fillers):

        feedback = []

        if wpm < 80:
            feedback.append("Speak slightly faster.")

        elif wpm > 160:
            feedback.append("Slow down your speaking pace.")

        else:
            feedback.append("Speaking speed is good.")

        if fillers == 0:
            feedback.append("Excellent fluency.")

        elif fillers <= 3:
            feedback.append("Very few filler words.")

        else:
            feedback.append("Reduce filler words.")

        return feedback