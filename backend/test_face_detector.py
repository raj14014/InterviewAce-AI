import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector

camera = Webcam()

detector = FaceDetector()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = detector.detect(frame)

    landmarks = detector.get_landmarks(results)

    if landmarks is not None:

        detector.draw(frame, landmarks)

        cv2.putText(
            frame,
            "Face Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
        )

    cv2.imshow("InterviewAce AI - Face Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()