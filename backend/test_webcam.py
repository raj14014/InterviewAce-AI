import cv2

from app.ai.webcam import Webcam

camera = Webcam()

while True:

    frame = camera.read()

    if frame is None:
        print("Could not read frame.")
        break

    cv2.imshow("InterviewAce AI Webcam", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()