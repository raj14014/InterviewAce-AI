"""
InterviewAce AI
Iris Detector
"""

import cv2

from app.ai.constants import LEFT_IRIS, RIGHT_IRIS
from app.ai.utils import landmark_to_pixel


class IrisDetector:

    def __init__(self):
        pass

    def get_iris_points(self, landmarks, width, height):

        left_iris = [
            landmark_to_pixel(landmarks.landmark[i], width, height)
            for i in LEFT_IRIS
        ]

        right_iris = [
            landmark_to_pixel(landmarks.landmark[i], width, height)
            for i in RIGHT_IRIS
        ]

        return left_iris, right_iris

    def iris_center(self, iris_points):

        x = sum(p[0] for p in iris_points) / len(iris_points)
        y = sum(p[1] for p in iris_points) / len(iris_points)

        return (int(x), int(y))

    def draw(self, frame, left_iris, right_iris):

        for point in left_iris:
            cv2.circle(frame, point, 2, (0, 255, 0), -1)

        for point in right_iris:
            cv2.circle(frame, point, 2, (0, 255, 0), -1)

        left_center = self.iris_center(left_iris)
        right_center = self.iris_center(right_iris)

        cv2.circle(frame, left_center, 5, (0, 0, 255), -1)
        cv2.circle(frame, right_center, 5, (0, 0, 255), -1)

        return left_center, right_center