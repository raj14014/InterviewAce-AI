import cv2

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.emotion_detector import EmotionDetector
from app.ai.emotion_tracker import EmotionTracker


camera = Webcam()
face_detector = FaceDetector()
emotion_detector = EmotionDetector()
emotion_tracker = EmotionTracker()


while True:

    frame = camera.read()

    if frame is None:
        break

    results = face_detector.detect(frame)

    landmarks = face_detector.get_landmarks(results)

    if landmarks is not None:

        h, w, _ = frame.shape

        bbox = face_detector.get_face_bbox(
            landmarks,
            w,
            h,
        )

        x, y, bw, bh = bbox

        # Crop face
        face = frame[y:y + bh, x:x + bw]

        emotion, confidence = emotion_detector.predict(face)

        # Update tracker
        emotion_tracker.update(emotion)

        stats = emotion_tracker.statistics()

        # Draw
        face_detector.draw(frame, landmarks)
        face_detector.draw_bbox(frame, bbox)

        cv2.putText(
            frame,
            f"Emotion : {emotion}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2,
        )

        cv2.putText(
            frame,
            f"Confidence : {confidence:.1f}%",
            (20,75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,0),
            2,
        )

        cv2.putText(
            frame,
            f"Dominant : {stats['dominant_emotion']}",
            (20,110),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,180,0),
            2,
        )

        cv2.putText(
            frame,
            f"Positivity : {stats['positivity']}%",
            (20,145),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,255),
            2,
        )

        cv2.putText(
            frame,
            f"Duration : {stats['duration']} sec",
            (20,180),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255,255,255),
            2,
        )

    cv2.imshow(
        "InterviewAce AI - Emotion Tracker",
        frame,
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()