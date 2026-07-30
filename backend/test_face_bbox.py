import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector


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

        # Draw face mesh
        face_detector.draw(frame, landmarks)

        # Get face bounding box
        bbox = face_detector.get_face_bbox(
            landmarks,
            w,
            h,
        )

        # Draw rectangle
        face_detector.draw_bbox(
            frame,
            bbox,
        )

        x, y, bw, bh = bbox

        cv2.putText(
            frame,
            f"W:{bw} H:{bh}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2,
        )

    cv2.imshow(
        "InterviewAce AI - Face Bounding Box",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()