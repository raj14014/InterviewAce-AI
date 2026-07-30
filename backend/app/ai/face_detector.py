"""
InterviewAce AI
Face Detector using MediaPipe Face Mesh
"""

import cv2
import mediapipe as mp

from app.ai.constants import (
    MAX_NUM_FACES,
    MIN_DETECTION_CONFIDENCE,
    MIN_TRACKING_CONFIDENCE,
)


class FaceDetector:
    """
    MediaPipe Face Mesh wrapper.
    Detects facial landmarks from an image.
    """

    def __init__(self):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=MAX_NUM_FACES,
            refine_landmarks=True,
            min_detection_confidence=MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=MIN_TRACKING_CONFIDENCE,
        )

        self.drawer = mp.solutions.drawing_utils

    def detect(self, frame):
        """
        Detect facial landmarks.
        """

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        return self.face_mesh.process(rgb)

    def get_landmarks(self, results):
        """
        Return first detected face landmarks.
        """

        if results.multi_face_landmarks:
            return results.multi_face_landmarks[0]

        return None

    def get_face_bbox(self, landmarks, width, height):
        """
        Compute face bounding box from landmarks.

        Returns:
            (x, y, w, h)
        """

        xs = [
            int(point.x * width)
            for point in landmarks.landmark
        ]

        ys = [
            int(point.y * height)
            for point in landmarks.landmark
        ]

        x = max(min(xs) - 20, 0)
        y = max(min(ys) - 20, 0)

        w = min(max(xs) + 20, width) - x
        h = min(max(ys) + 20, height) - y

        return (x, y, w, h)

    def draw(self, frame, landmarks):
        """
        Draw face mesh.
        """

        self.drawer.draw_landmarks(
            image=frame,
            landmark_list=landmarks,
            connections=self.mp_face_mesh.FACEMESH_TESSELATION,
            landmark_drawing_spec=None,
            connection_drawing_spec=self.drawer.DrawingSpec(
                color=(0, 255, 0),
                thickness=1,
                circle_radius=1,
            ),
        )

        return frame

    def draw_bbox(self, frame, bbox):
        """
        Draw face bounding box.
        """

        x, y, w, h = bbox

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2,
        )

        return frame