import re


class VoiceAnalyzer:
    """
    Analyze spoken text and estimate communication quality.
    """

    FILLER_WORDS = [
        "um",
        "uh",
        "like",
        "actually",
        "basically",
        "you know",
        "hmm",
    ]

    def analyze(
        self,
        transcript: str,
        duration_seconds: float,
    ):
        transcript = transcript.lower()

        words = transcript.split()

        word_count = len(words)

        # Speaking speed
        minutes = max(duration_seconds / 60, 0.01)
        wpm = round(word_count / minutes)

        # Count fillers
        filler_count = 0

        for filler in self.FILLER_WORDS:
            filler_count += len(
                re.findall(
                    r"\b" + re.escape(filler) + r"\b",
                    transcript,
                )
            )

        # Pause estimation
        pause_count = transcript.count("...")

        # Confidence score
        score = 100

        score -= filler_count * 3
        score -= pause_count * 2

        if wpm < 90:
            score -= 10

        elif wpm > 170:
            score -= 10

        score = max(0, min(100, score))

        # Rating
        if score >= 90:
            rating = "Excellent"

        elif score >= 75:
            rating = "Good"

        elif score >= 60:
            rating = "Average"

        else:
            rating = "Needs Improvement"

        return {
            "words": word_count,
            "wpm": wpm,
            "fillers": filler_count,
            "pauses": pause_count,
            "confidence_score": score,
            "rating": rating,
        }