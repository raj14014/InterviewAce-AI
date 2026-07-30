import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.iris_detector import IrisDetector

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

        face_detector.draw(frame, landmarks)

        h, w, _ = frame.shape

        left_iris, right_iris = iris_detector.get_iris_points(
            landmarks,
            w,
            h
        )

        iris_detector.draw(
            frame,
            left_iris,
            right_iris
        )

        cv2.putText(
            frame,
            "Iris Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    cv2.imshow("InterviewAce AI - Iris Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()