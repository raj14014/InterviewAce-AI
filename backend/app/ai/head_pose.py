"""
InterviewAce AI
Professional Head Pose Estimator
"""

import numpy as np

from app.ai.constants import (
    NOSE_TIP,
    CHIN,
    LEFT_FACE,
    RIGHT_FACE,
)


class HeadPose:

    def __init__(self):
        pass

    def estimate(self, landmarks, width, height):
        """
        Returns:

        yaw
        pitch
        direction
        stability
        """

        nose = landmarks.landmark[NOSE_TIP]
        chin = landmarks.landmark[CHIN]
        left_face = landmarks.landmark[LEFT_FACE]
        right_face = landmarks.landmark[RIGHT_FACE]

        nose = np.array([
            nose.x * width,
            nose.y * height
        ])

        chin = np.array([
            chin.x * width,
            chin.y * height
        ])

        left_face = np.array([
            left_face.x * width,
            left_face.y * height
        ])

        right_face = np.array([
            right_face.x * width,
            right_face.y * height
        ])

        face_center = (left_face + right_face) / 2

        face_width = right_face[0] - left_face[0]

        if abs(face_width) < 1:
            face_width = 1

        yaw = (nose[0] - face_center[0]) / face_width

        pitch = (nose[1] - face_center[1]) / face_width

        # ----------------------------
        # Direction
        # ----------------------------

        if yaw < -0.08:
            direction = "Looking Left"

        elif yaw > 0.08:
            direction = "Looking Right"

        else:
            direction = "Looking Straight"

        # ----------------------------
        # Stability
        # ----------------------------

        stability = max(
            0,
            100 - (
                abs(yaw) * 350
                + abs(pitch) * 180
            )
        )

        return (
            yaw,
            pitch,
            direction,
            round(stability, 1),
        )