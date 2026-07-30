from typing import Dict


def calculate_emotion_score(emotion: str) -> int:
    """
    Returns score based on detected emotion.
    """

    scores = {
        "happy": 10,
        "neutral": 8,
        "surprise": 7,
        "sad": 4,
        "fear": 3,
        "angry": 2,
        "disgust": 1
    }

    return scores.get(emotion.lower(), 5)


def calculate_eye_contact_score(percentage: float) -> int:

    if percentage >= 90:
        return 10
    elif percentage >= 75:
        return 8
    elif percentage >= 60:
        return 6
    elif percentage >= 40:
        return 4
    else:
        return 2


def calculate_speech_score(wpm: int) -> int:

    if 110 <= wpm <= 150:
        return 10
    elif 90 <= wpm <= 170:
        return 8
    elif 70 <= wpm <= 190:
        return 6
    else:
        return 4


def calculate_confidence(
    emotion_score: int,
    eye_score: int,
    speech_score: int
) -> float:

    return round(
        (emotion_score + eye_score + speech_score) / 3,
        2
    )


def generate_feedback(confidence: float) -> str:

    if confidence >= 9:
        return "Excellent interview performance."
    elif confidence >= 8:
        return "Very Good. Minor improvements required."
    elif confidence >= 7:
        return "Good performance. Improve eye contact."
    elif confidence >= 5:
        return "Average performance. Practice speaking confidently."
    else:
        return "Needs Improvement. Practice mock interviews."