"""
InterviewAce AI
Eye Contact Session Tracker
"""

import time


class EyeContactTracker:

    def __init__(self):

        self.start_time = time.time()

        self.total_frames = 0
        self.camera_frames = 0

        self.current_score = 100.0
        self.smoothed_score = 100.0

        # Exponential Moving Average factor
        self.alpha = 0.10

    def update(self, direction, score):
        """
        Update statistics for each frame.
        """

        self.total_frames += 1

        if direction == "Looking At Camera":
            self.camera_frames += 1

        self.current_score = score

        self.smoothed_score = (
            self.alpha * score
            + (1 - self.alpha) * self.smoothed_score
        )

    def eye_contact_percentage(self):

        if self.total_frames == 0:
            return 0.0

        return round(
            (self.camera_frames / self.total_frames) * 100,
            1,
        )

    def live_score(self):

        return round(self.smoothed_score, 1)

    def session_duration(self):

        return round(
            time.time() - self.start_time,
            1,
        )

    def statistics(self):

        return {
            "duration": self.session_duration(),
            "frames": self.total_frames,
            "camera_frames": self.camera_frames,
            "eye_contact": self.eye_contact_percentage(),
            "live_score": self.live_score(),
        }

    def reset(self):

        self.__init__()