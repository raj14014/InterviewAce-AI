"""
InterviewAce AI
Eye Contact Analyzer
"""

from app.ai.constants import (
    LOOKING_LEFT_THRESHOLD,
    LOOKING_RIGHT_THRESHOLD,
    PERFECT_CONTACT_MIN,
    PERFECT_CONTACT_MAX,
)


class EyeContactAI:

    @staticmethod
    def get_direction(ratio):
        """
        Determine gaze direction.
        """

        if ratio < LOOKING_LEFT_THRESHOLD:
            return "Looking Left"

        if ratio > LOOKING_RIGHT_THRESHOLD:
            return "Looking Right"

        return "Looking At Camera"

    @staticmethod
    def eye_contact_score(ratio):
        """
        Convert gaze ratio into
        eye contact score (0-100).
        """

        center = 0.50

        error = abs(ratio - center)

        score = max(0, 100 - error * 250)

        return round(score, 1)

    @staticmethod
    def confidence(ratio):
        """
        Confidence that user is
        looking toward camera.
        """

        if PERFECT_CONTACT_MIN <= ratio <= PERFECT_CONTACT_MAX:
            return 100.0

        distance = abs(ratio - 0.50)

        confidence = max(0, 100 - distance * 300)

        return round(confidence, 1)