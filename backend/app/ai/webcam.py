"""
InterviewAce AI
Webcam Manager
"""

import cv2

from app.ai.constants import (
    CAMERA_ID,
    FRAME_WIDTH,
    FRAME_HEIGHT
)


class Webcam:

    def __init__(self):

        self.cap = cv2.VideoCapture(
            CAMERA_ID,
            cv2.CAP_DSHOW
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            FRAME_WIDTH
        )

        self.cap.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            FRAME_HEIGHT
        )

    def read(self):
        """
        Read one frame.
        """

        success, frame = self.cap.read()

        if not success:
            return None

        frame = cv2.flip(frame, 1)

        return frame

    def release(self):
        """
        Release camera.
        """

        self.cap.release()
        cv2.destroyAllWindows()