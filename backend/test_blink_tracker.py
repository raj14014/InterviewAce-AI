import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.blink_detector import BlinkDetector
from app.ai.blink_tracker import BlinkTracker

from app.ai.constants import (
    LEFT_EYE_OUTER,
    LEFT_EYE_INNER,
    LEFT_UPPER_EYELID,
    LEFT_LOWER_EYELID,
    RIGHT_EYE_OUTER,
    RIGHT_EYE_INNER,
    RIGHT_UPPER_EYELID,
    RIGHT_LOWER_EYELID,
)

from app.ai.utils import landmark_to_pixel


camera = Webcam()
face_detector = FaceDetector()
blink_detector = BlinkDetector()
tracker = BlinkTracker()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)
    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        left_upper = landmark_to_pixel(
            landmarks.landmark[LEFT_UPPER_EYELID], w, h
        )

        left_lower = landmark_to_pixel(
            landmarks.landmark[LEFT_LOWER_EYELID], w, h
        )

        left_outer = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_OUTER], w, h
        )

        left_inner = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_INNER], w, h
        )

        right_upper = landmark_to_pixel(
            landmarks.landmark[RIGHT_UPPER_EYELID], w, h
        )

        right_lower = landmark_to_pixel(
            landmarks.landmark[RIGHT_LOWER_EYELID], w, h
        )

        right_outer = landmark_to_pixel(
            landmarks.landmark[RIGHT_EYE_OUTER], w, h
        )

        right_inner = landmark_to_pixel(
            landmarks.landmark[RIGHT_EYE_INNER], w, h
        )

        ear, blinks = blink_detector.detect(
            left_upper,
            left_lower,
            left_outer,
            left_inner,
            right_upper,
            right_lower,
            right_outer,
            right_inner,
        )

        tracker.update(blinks)

        stats = tracker.statistics()

        eye_status = "OPEN"

        if ear < 0.21:
            eye_status = "CLOSED"

        cv2.putText(
            frame,
            f"EAR : {ear:.3f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Eye : {eye_status}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Blinks : {stats['blinks']}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Blink Rate : {stats['blink_rate']}/min",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Duration : {stats['duration']} sec",
            (20, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 165, 255),
            2,
        )

    cv2.imshow(
        "InterviewAce AI - Blink Tracker",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()