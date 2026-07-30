"""
InterviewAce AI
Speech Analyzer
"""

import whisper


class SpeechAnalyzer:

    def __init__(self):

        print("Loading Whisper Model...")

        self.model = whisper.load_model("base")

        print("Whisper Ready.")

    # -------------------------------------
    # Speech to Text
    # -------------------------------------

    def transcribe(self, audio_path):

        result = self.model.transcribe(
            audio_path,
            language="en",
            fp16=False,
        )

        return result["text"].strip()

    # -------------------------------------
    # Words Per Minute
    # -------------------------------------

    def words_per_minute(
        self,
        text,
        duration,
    ):

        words = len(text.split())

        if duration == 0:
            return 0

        return round(words / (duration / 60), 1)

    # -------------------------------------
    # Filler Words
    # -------------------------------------

    def filler_words(self, text):

        fillers = [
            "um",
            "uh",
            "like",
            "you know",
            "actually",
            "basically",
            "so",
        ]

        text = text.lower()

        count = 0

        for word in fillers:

            count += text.count(word)

        return count

    # -------------------------------------
    # Analyze
    # -------------------------------------

    def analyze(
        self,
        audio_path,
        duration,
    ):

        text = self.transcribe(audio_path)

        return {

            "text": text,

            "wpm": self.words_per_minute(
                text,
                duration,
            ),

            "fillers": self.filler_words(text),

        }