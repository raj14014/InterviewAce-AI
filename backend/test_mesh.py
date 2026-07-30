import cv2

from app.vision.camera import Camera
from app.vision.face_mesh import FaceMeshDetector

camera = Camera()

mesh = FaceMeshDetector()

while True:

    success, frame = camera.read()

    if not success:
        break

    result = mesh.process(frame)

    frame = mesh.draw(
        frame,
        result,
    )

    cv2.imshow(
        "InterviewAce AI Face Mesh",
        frame,
    )

    if cv2.waitKey(1) == 27:
        break

camera.release()

cv2.destroyAllWindows()