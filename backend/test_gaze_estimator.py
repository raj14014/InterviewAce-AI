import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.iris_detector import IrisDetector
from app.ai.gaze_estimator import GazeEstimator

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

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)
    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        left_iris, right_iris = iris_detector.get_iris_points(
            landmarks, w, h
        )

        left_center, right_center = iris_detector.draw(
            frame,
            left_iris,
            right_iris,
        )
        
        cv2.putText(
        frame,
        "RED = Iris Center",
        (20, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2,
        )

        left_outer = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_OUTER], w, h
        )

        left_inner = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_INNER], w, h
        )

        right_outer = landmark_to_pixel(
            landmarks.landmark[RIGHT_EYE_OUTER], w, h
        )

        right_inner = landmark_to_pixel(
            landmarks.landmark[RIGHT_EYE_INNER], w, h
        )
        
        print("------------------------------")
        print("Left Center :", left_center)
        print("Right Center:", right_center)
        print("Left Outer  :", left_outer)
        print("Left Inner  :", left_inner)
        print("Right Outer :", right_outer)
        print("Right Inner :", right_inner)

        ratio, left_ratio, right_ratio = GazeEstimator.estimate(
            left_center,
            right_center,
            left_outer,
            left_inner,
            right_outer,
            right_inner,
        )

        cv2.putText(
            frame,
            f"Avg Ratio : {ratio:.2f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Left Ratio : {left_ratio:.2f}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Right Ratio : {right_ratio:.2f}",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 0),
            2,
        )

    cv2.imshow("InterviewAce AI - Gaze Estimator Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()