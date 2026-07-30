import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.head_pose import HeadPose
from app.ai.head_pose_tracker import HeadPoseTracker


camera = Webcam()
face_detector = FaceDetector()
head_pose = HeadPose()
tracker = HeadPoseTracker()

while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)
    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        yaw, pitch = head_pose.estimate(
            landmarks,
            w,
            h,
        )

        # Determine direction
        if yaw < -0.08:
            direction = "Looking Left"
        elif yaw > 0.08:
            direction = "Looking Right"
        else:
            direction = "Looking Straight"

        tracker.update(direction)

        stats = tracker.statistics()

        cv2.putText(
            frame,
            f"Yaw : {yaw:.3f}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Pitch : {pitch:.1f}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            frame,
            f"Direction : {direction}",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Attention : {stats['attention']}%",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            frame,
            f"Duration : {stats['duration']} sec",
            (20, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 165, 255),
            2,
        )

    cv2.imshow(
        "InterviewAce AI - Head Pose Tracker",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()