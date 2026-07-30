"""
InterviewAce AI
Interview Analyzer
"""

import time


class InterviewAnalyzer:

    def __init__(self):

        self.start_time = time.time()

        self.eye_contact = 0.0
        self.blink_rate = 0.0
        self.head_stability = 0.0

        self.emotion = "Unknown"
        self.emotion_score = 0.0

    # ---------------------------------
    # Update Methods
    # ---------------------------------

    def update_eye_contact(self, percentage):
        self.eye_contact = percentage

    def update_blink_rate(self, rate):
        self.blink_rate = rate

    def update_head_stability(self, stability):
        self.head_stability = stability

    def update_emotion(self, emotion, positivity):
        self.emotion = emotion
        self.emotion_score = positivity

    # ---------------------------------
    # Duration
    # ---------------------------------

    def duration(self):
        return round(time.time() - self.start_time, 1)

    # ---------------------------------
    # Scores
    # ---------------------------------

    def eye_contact_score(self):
        return min(25, self.eye_contact * 25 / 100)

    def blink_score(self):

        if 12 <= self.blink_rate <= 20:
            return 15

        if 8 <= self.blink_rate < 12:
            return 12

        if 20 < self.blink_rate <= 25:
            return 12

        return 8

    def head_pose_score(self):
        return min(20, self.head_stability * 20 / 100)

    def emotion_score_value(self):
        return min(20, self.emotion_score * 20 / 100)

    def confidence_score(self):

        return (
            self.eye_contact_score()
            + self.head_pose_score()
        ) / 45 * 20

    def overall_score(self):

        score = (

            self.eye_contact_score()

            + self.blink_score()

            + self.head_pose_score()

            + self.emotion_score_value()

            + self.confidence_score()

        )

        return round(score, 1)

    # ---------------------------------
    # AI Feedback
    # ---------------------------------

    def generate_feedback(self):

        feedback = []

        if self.eye_contact >= 90:
            feedback.append("Excellent eye contact.")
        elif self.eye_contact >= 75:
            feedback.append("Good eye contact. Try maintaining it consistently.")
        else:
            feedback.append("Maintain better eye contact with the interviewer.")

        if 12 <= self.blink_rate <= 20:
            feedback.append("Blink rate is normal.")
        else:
            feedback.append("Try to blink naturally.")

        if self.head_stability >= 85:
            feedback.append("Head posture is stable.")
        else:
            feedback.append("Reduce unnecessary head movement.")

        if self.emotion.lower() in ["happy", "neutral"]:
            feedback.append("Positive facial expression maintained.")
        else:
            feedback.append("Try maintaining a calm, confident expression.")

        return feedback

    # ---------------------------------
    # Report
    # ---------------------------------

    def generate_report(self):

        return {

            "duration": self.duration(),

            "eye_contact": self.eye_contact,

            "blink_rate": self.blink_rate,

            "head_stability": self.head_stability,

            "emotion": self.emotion,

            "positivity": self.emotion_score,

            "overall_score": self.overall_score(),

            "feedback": self.generate_feedback(),

        }