"""
InterviewAce AI
Emotion Detector
"""

import cv2

from transformers import pipeline


class EmotionDetector:

    def __init__(self):

        print("Loading Emotion Model...")

        self.classifier = pipeline(
            task="image-classification",
            model="trpakov/vit-face-expression"
        )

        print("Emotion Model Loaded.")

    def predict(self, face_image):
        """
        Predict emotion from a cropped face image.

        Returns:
            emotion (str)
            confidence (float)
        """

        if face_image is None or face_image.size == 0:
            return "Unknown", 0.0

        rgb = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)

        result = self.classifier(rgb)

        emotion = result[0]["label"]
        confidence = result[0]["score"] * 100

        return emotion, confidence