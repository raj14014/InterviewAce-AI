import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.iris_detector import IrisDetector
from app.ai.constants import (
    LEFT_EYE_OUTER,
    LEFT_EYE_INNER,
)
from app.ai.utils import landmark_to_pixel

camera = Webcam()
face = FaceDetector()
iris = IrisDetector()

while True:

    frame = camera.read()

    results = face.detect(frame)
    landmarks = face.get_landmarks(results)

    if landmarks:

        h, w, _ = frame.shape

        left_iris, right_iris = iris.get_iris_points(
            landmarks,
            w,
            h
        )

        left_center, _ = iris.draw(
            frame,
            left_iris,
            right_iris
        )

        outer = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_OUTER],
            w,
            h
        )

        inner = landmark_to_pixel(
            landmarks.landmark[LEFT_EYE_INNER],
            w,
            h
        )

        cv2.circle(frame, outer, 6, (255,0,0), -1)
        cv2.circle(frame, inner, 6, (0,255,0), -1)

        print(
            f"Outer={outer[0]}  Iris={left_center[0]}  Inner={inner[0]}"
        )

    cv2.imshow("Debug", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()