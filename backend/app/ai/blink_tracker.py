"""
InterviewAce AI
Blink Statistics Tracker
"""

import time


class BlinkTracker:

    def __init__(self):

        self.start_time = time.time()

        self.total_blinks = 0

        self.last_blinks = 0

    def update(self, current_blinks):

        if current_blinks > self.last_blinks:

            self.total_blinks += (
                current_blinks - self.last_blinks
            )

            self.last_blinks = current_blinks

    def duration(self):

        return time.time() - self.start_time

    def blink_rate(self):

        minutes = self.duration() / 60

        if minutes == 0:
            return 0

        return round(self.total_blinks / minutes, 1)

    def statistics(self):

        return {
            "duration": round(self.duration(), 1),
            "blinks": self.total_blinks,
            "blink_rate": self.blink_rate(),
        }

    def reset(self):

        self.__init__()