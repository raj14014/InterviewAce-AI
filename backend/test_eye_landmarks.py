import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.utils import landmark_to_pixel

from app.ai.constants import (
    LEFT_EYE_OUTER,
    LEFT_EYE_INNER,
    RIGHT_EYE_OUTER,
    RIGHT_EYE_INNER,
)

camera = Webcam()
face_detector = FaceDetector()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)

    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        left_outer = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_OUTER],
            w,
            h,
        )

        left_inner = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_INNER],
            w,
            h,
        )

        right_outer = landmark_to_pixel(
            landmarks.landmark[RIGHT_EYE_OUTER],
            w,
            h,
        )

        right_inner = landmark_to_pixel(
            landmarks.landmark[RIGHT_EYE_INNER],
            w,
            h,
        )

        cv2.circle(frame, left_outer, 6, (255, 0, 0), -1)
        cv2.circle(frame, left_inner, 6, (0, 255, 0), -1)

        cv2.circle(frame, right_outer, 6, (255, 0, 0), -1)
        cv2.circle(frame, right_inner, 6, (0, 255, 0), -1)

        cv2.putText(
            frame,
            "Blue = Outer  |  Green = Inner",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

    cv2.imshow("Eye Corner Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()