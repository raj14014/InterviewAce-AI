"""
InterviewAce AI
Utility Functions
"""

import math
import time


def landmark_to_pixel(landmark, width, height):
    """
    Convert MediaPipe normalized landmark
    into pixel coordinates.
    """
    return (
        int(landmark.x * width),
        int(landmark.y * height)
    )


def distance(point1, point2):
    """
    Euclidean distance between two points.
    """

    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2
    )


def midpoint(point1, point2):
    """
    Midpoint of two coordinates.
    """

    return (
        int((point1[0] + point2[0]) / 2),
        int((point1[1] + point2[1]) / 2)
    )


class FPSCounter:
    """
    Calculates real-time FPS.
    """

    def __init__(self):

        self.previous_time = time.time()

    def get_fps(self):

        current_time = time.time()

        fps = 1 / (current_time - self.previous_time)

        self.previous_time = current_time

        return int(fps)