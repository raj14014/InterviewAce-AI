import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.iris_detector import IrisDetector
from app.ai.gaze_estimator import GazeEstimator
from app.ai.eye_contact import EyeContactAI
from app.ai.eye_contact_tracker import EyeContactTracker

from app.ai.constants import (
    LEFT_EYE_OUTER,
    LEFT_EYE_INNER,
    RIGHT_EYE_OUTER,
    RIGHT_EYE_INNER,
)

from app.ai.utils import landmark_to_pixel


camera = Webcam()
face_detector = FaceDetector()
iris_detector = IrisDetector()
tracker = EyeContactTracker()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)
    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        left_iris, right_iris = iris_detector.get_iris_points(
            landmarks,
            w,
            h,
        )

        left_center, right_center = iris_detector.draw(
            frame,
            left_iris,
            right_iris,
        )

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

        ratio, left_ratio, right_ratio = GazeEstimator.estimate(
            left_center,
            right_center,
            left_outer,
            left_inner,
            right_outer,
            right_inner,
        )

        direction = EyeContactAI.get_direction(ratio)

        score = EyeContactAI.eye_contact_score(ratio)

        confidence = EyeContactAI.confidence(ratio)

        tracker.update(direction, score)

        stats = tracker.statistics()

        cv2.putText(
            frame,
            f"Direction : {direction}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Live Score : {stats['live_score']}%",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Session Eye Contact : {stats['eye_contact']}%",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Confidence : {confidence:.1f}%",
            (20, 145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Duration : {stats['duration']} sec",
            (20, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 165, 255),
            2,
        )

    cv2.imshow(
        "InterviewAce AI - Eye Contact Tracker",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()