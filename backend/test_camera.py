import cv2

from app.vision.camera import Camera
from app.vision.face_detector import FaceDetector

camera = Camera()

detector = FaceDetector()

while True:

    success, frame = camera.read()

    if not success:
        break

    result = detector.detect(frame)

    if result.detections:

        for detection in result.detections:

            box = detection.location_data.relative_bounding_box

            h, w, _ = frame.shape

            x = int(box.xmin * w)
            y = int(box.ymin * h)
            bw = int(box.width * w)
            bh = int(box.height * h)

            cv2.rectangle(
                frame,
                (x, y),
                (x + bw, y + bh),
                (0, 255, 0),
                2,
            )

    cv2.imshow(
        "InterviewAce AI",
        frame,
    )

    if cv2.waitKey(1) == 27:
        break

camera.release()

cv2.destroyAllWindows()