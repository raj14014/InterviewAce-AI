"""
InterviewAce AI
Professional Blink Detector
"""

from app.ai.constants import (
    LEFT_UPPER_EYELID,
    LEFT_LOWER_EYELID,
    RIGHT_UPPER_EYELID,
    RIGHT_LOWER_EYELID,
    EAR_THRESHOLD,
    EAR_CONSECUTIVE_FRAMES,
)

from app.ai.utils import distance


class BlinkDetector:

    def __init__(self):

        self.total_blinks = 0

        self.closed_frames = 0

        self.eye_closed = False

    def eye_aspect_ratio(
        self,
        upper,
        lower,
        outer,
        inner,
    ):
        """
        Eye Aspect Ratio (EAR)

        vertical distance
        -----------------
        horizontal distance
        """

        vertical = distance(
            upper,
            lower,
        )

        horizontal = distance(
            outer,
            inner,
        )

        if horizontal == 0:
            return 0

        return vertical / horizontal

    def detect(
        self,
        left_upper,
        left_lower,
        left_outer,
        left_inner,
        right_upper,
        right_lower,
        right_outer,
        right_inner,
    ):

        left_ear = self.eye_aspect_ratio(
            left_upper,
            left_lower,
            left_outer,
            left_inner,
        )

        right_ear = self.eye_aspect_ratio(
            right_upper,
            right_lower,
            right_outer,
            right_inner,
        )

        ear = (left_ear + right_ear) / 2

        if ear < EAR_THRESHOLD:

            self.closed_frames += 1

        else:

            if (
                self.closed_frames >=
                EAR_CONSECUTIVE_FRAMES
            ):
                self.total_blinks += 1

            self.closed_frames = 0

        return (
            ear,
            self.total_blinks,
        )