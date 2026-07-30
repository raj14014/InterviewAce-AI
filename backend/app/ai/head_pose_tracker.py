"""
InterviewAce AI
Head Pose Session Tracker
"""

import time


class HeadPoseTracker:

    def __init__(self):

        self.start_time = time.time()

        self.total_frames = 0

        self.straight_frames = 0
        self.left_frames = 0
        self.right_frames = 0

    def update(self, direction):

        self.total_frames += 1

        if direction == "Looking Straight":
            self.straight_frames += 1

        elif direction == "Looking Left":
            self.left_frames += 1

        elif direction == "Looking Right":
            self.right_frames += 1

    def duration(self):

        return round(
            time.time() - self.start_time,
            1
        )

    def attention_score(self):

        if self.total_frames == 0:
            return 0.0

        return round(
            self.straight_frames / self.total_frames * 100,
            1
        )

    def statistics(self):

        return {

            "duration": self.duration(),

            "straight": self.straight_frames,

            "left": self.left_frames,

            "right": self.right_frames,

            "attention": self.attention_score(),
        }

    def reset(self):

        self.__init__()