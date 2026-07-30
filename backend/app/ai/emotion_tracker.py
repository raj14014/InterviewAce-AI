"""
InterviewAce AI
Emotion Session Tracker
"""

import time
from collections import Counter


class EmotionTracker:

    def __init__(self):

        self.start_time = time.time()

        self.total_frames = 0

        self.emotions = []

        self.current_emotion = "Unknown"

    def update(self, emotion):

        self.total_frames += 1

        self.current_emotion = emotion

        self.emotions.append(emotion)

    def dominant_emotion(self):

        if not self.emotions:
            return "Unknown"

        return Counter(self.emotions).most_common(1)[0][0]

    def positivity_score(self):

        if self.total_frames == 0:
            return 0

        positive = 0

        for emotion in self.emotions:

            if emotion.lower() in [
                "happy",
                "surprise",
                "neutral",
            ]:
                positive += 1

        return round(
            positive / self.total_frames * 100,
            1,
        )

    def duration(self):

        return round(
            time.time() - self.start_time,
            1,
        )

    def statistics(self):

        return {
            "duration": self.duration(),
            "frames": self.total_frames,
            "dominant_emotion": self.dominant_emotion(),
            "positivity": self.positivity_score(),
        }

    def reset(self):

        self.__init__()