import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.head_pose import HeadPose


camera = Webcam()
face_detector = FaceDetector()
head_pose = HeadPose()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)

    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        face_detector.draw(frame, landmarks)

        yaw, pitch, direction, stability = head_pose.estimate(
            landmarks,
            w,
            h,
        )

        cv2.putText(
            frame,
            f"Direction : {direction}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Yaw : {yaw:.3f}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Pitch : {pitch:.3f}",
            (20, 110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Stability : {stability:.1f}%",
            (20, 145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 180, 0),
            2,
        )

    cv2.imshow(
        "InterviewAce AI - Head Pose V2",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()