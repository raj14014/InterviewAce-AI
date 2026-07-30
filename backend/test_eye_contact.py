import cv2

from app.vision.camera import Camera
from app.vision.face_mesh import FaceMeshDetector
from app.vision.eye_contact import EyeContactDetector

camera = Camera()

mesh = FaceMeshDetector()

eye = EyeContactDetector()

while True:

    success, frame = camera.read()

    if not success:
        break

    result = mesh.process(frame)

    frame = mesh.draw(frame, result)

    analysis = eye.analyze(frame, result)

    cv2.putText(
        frame,
        f"Eye Contact: {analysis['score']}%",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow(
        "InterviewAce Eye Contact",
        frame,
    )

    if cv2.waitKey(1) == 27:
        break

camera.release()

cv2.destroyAllWindows()