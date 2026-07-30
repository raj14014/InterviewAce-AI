"""
InterviewAce AI
Production AI Engine
"""

import cv2

import time

from app.ai.webcam import Webcam
from app.ai.face_detector import FaceDetector
from app.ai.iris_detector import IrisDetector
from app.ai.gaze_estimator import GazeEstimator

from app.ai.eye_contact import EyeContactAI
from app.ai.eye_contact_tracker import EyeContactTracker

from app.ai.blink_detector import BlinkDetector
from app.ai.blink_tracker import BlinkTracker

from app.ai.head_pose import HeadPose
from app.ai.head_pose_tracker import HeadPoseTracker

from app.ai.emotion_detector import EmotionDetector
from app.ai.emotion_tracker import EmotionTracker

from app.ai.interview_analyzer import InterviewAnalyzer

from app.ai.speech_recorder import SpeechRecorder
from app.ai.speech_analyzer import SpeechAnalyzer
from app.ai.speech_tracker import SpeechTracker

from app.ai.interview_manager import InterviewManager

from app.ai.communication_analyzer import CommunicationAnalyzer

from app.ai.voice_interviewer import VoiceInterviewer

from app.ai.live_score import LiveScore

from app.ai.answer_evaluator import AnswerEvaluator

from app.report.pdf_report import PDFReport

from app.database.interview_history import InterviewHistory

from app.ai.utils import (
    landmark_to_pixel,
    FPSCounter,
)

from app.ai.constants import (
    LEFT_EYE_OUTER,
    LEFT_EYE_INNER,
    RIGHT_EYE_OUTER,
    RIGHT_EYE_INNER,
    LEFT_UPPER_EYELID,
    LEFT_LOWER_EYELID,
    RIGHT_UPPER_EYELID,
    RIGHT_LOWER_EYELID,
)

class AIEngine:

    def __init__(self):

        print("=" * 60)
        print(" InterviewAce AI")
        print(" Production AI Engine")
        print("=" * 60)

        # Camera
        self.camera = Webcam()

        # Face
        self.face_detector = FaceDetector()

        # Iris
        self.iris_detector = IrisDetector()

        # Gaze
        self.gaze_estimator = GazeEstimator()

        # Eye Contact
        self.eye_ai = EyeContactAI()
        self.eye_tracker = EyeContactTracker()

        # Blink
        self.blink_detector = BlinkDetector()
        self.blink_tracker = BlinkTracker()

        # Head Pose
        self.head_pose = HeadPose()
        self.head_tracker = HeadPoseTracker()

        # Emotion
        self.emotion_detector = EmotionDetector()
        self.emotion_tracker = EmotionTracker()

        # Interview Analyzer
        self.analyzer = InterviewAnalyzer()
        
        self.speech = SpeechRecorder()

        self.speech_ai = SpeechAnalyzer()

        self.speech_result = None
        
        # Voice Interviewer
        self.voice = VoiceInterviewer()
        
        self.evaluator = AnswerEvaluator()
        
        self.communication = CommunicationAnalyzer()
        
        self.live_score = LiveScore()
        
        # Interview Manager
        self.interview = InterviewManager()

        self.communication_score = 0

        self.communication_feedback = []

        self.question_start = time.time()

        self.question_duration = 45
        
        self.ai_feedback = "Waiting for answer..."
        
        self.pdf = PDFReport()
        
        self.history = InterviewHistory()

        # FPS
        self.fps = FPSCounter()

        # Runtime Variables
        self.frame = None
        self.results = None
        self.landmarks = None

        self.width = 0
        self.height = 0

        self.left_center = None
        self.right_center = None

        self.left_ratio = 0.0
        self.right_ratio = 0.0
        self.gaze_ratio = 0.0

        self.eye_direction = ""
        self.eye_score = 0.0

        self.ear = 0.0
        self.total_blinks = 0

        self.yaw = 0.0
        self.pitch = 0.0
        self.head_direction = ""
        self.head_stability = 0.0

        self.emotion = "Neutral"
        self.emotion_confidence = 0.0

        print("AI Engine Ready.")

    # ==========================================
    # Camera
    # ==========================================

    def read_frame(self):

        self.frame = self.camera.read()

        if self.frame is None:
            return False

        self.height, self.width, _ = self.frame.shape

        return True

    # ==========================================
    # Face Detection
    # ==========================================

    def process_face(self):

        self.results = self.face_detector.detect(
            self.frame
        )

        self.landmarks = self.face_detector.get_landmarks(
            self.results
        )

        if self.landmarks is None:
            return False

        self.face_detector.draw(
            self.frame,
            self.landmarks,
        )

        return True
    
    # ==========================================
    # Iris Detection
    # ==========================================

    def process_iris(self):

        self.left_iris, self.right_iris = (
            self.iris_detector.get_iris_points(
                self.landmarks,
                self.width,
                self.height,
            )
        )

        (
            self.left_center,
            self.right_center,
        ) = self.iris_detector.draw(
            self.frame,
            self.left_iris,
            self.right_iris,
        )

        return True

    # ==========================================
    # Gaze Estimation
    # ==========================================

    def process_gaze(self):

        left_outer = landmark_to_pixel(
            self.landmarks.landmark[LEFT_EYE_OUTER],
            self.width,
            self.height,
        )

        left_inner = landmark_to_pixel(
            self.landmarks.landmark[LEFT_EYE_INNER],
            self.width,
            self.height,
        )

        right_outer = landmark_to_pixel(
            self.landmarks.landmark[RIGHT_EYE_OUTER],
            self.width,
            self.height,
        )

        right_inner = landmark_to_pixel(
            self.landmarks.landmark[RIGHT_EYE_INNER],
            self.width,
            self.height,
        )

        (
            self.gaze_ratio,
            self.left_ratio,
            self.right_ratio,
        ) = self.gaze_estimator.estimate(
            self.left_center,
            self.right_center,
            left_outer,
            left_inner,
            right_outer,
            right_inner,
        )

        return True
    
    # ==========================================
    # Eye Contact
    # ==========================================

    def process_eye_contact(self):

        # Direction
        self.eye_direction = self.eye_ai.get_direction(
            self.gaze_ratio
        )

        # Current Score
        self.eye_score = self.eye_ai.eye_contact_score(
            self.gaze_ratio
        )

        # Update Session Tracker
        self.eye_tracker.update(
            self.eye_direction,
            self.eye_score,
        )

        return True
    
    # ==========================================
    # Eye Contact Dashboard
    # ==========================================

    def draw_eye_dashboard(self):

        stats = self.eye_tracker.statistics()

        cv2.putText(
            self.frame,
            f"Direction : {self.eye_direction}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            self.frame,
            f"Gaze Ratio : {self.gaze_ratio:.2f}",
            (20, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )

        cv2.putText(
            self.frame,
            f"Eye Score : {self.eye_score:.1f}",
            (20, 95),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 200, 0),
            2,
        )

        cv2.putText(
            self.frame,
            f"Eye Contact : {stats['eye_contact']:.1f}%",
            (20, 125),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2,
        )
        
    # ==========================================
    # Blink Detection
    # ==========================================

    def process_blink(self):

        left_upper = landmark_to_pixel(
            self.landmarks.landmark[LEFT_UPPER_EYELID],
            self.width,
            self.height,
        )

        left_lower = landmark_to_pixel(
            self.landmarks.landmark[LEFT_LOWER_EYELID],
            self.width,
            self.height,
        )

        left_outer = landmark_to_pixel(
            self.landmarks.landmark[LEFT_EYE_OUTER],
            self.width,
            self.height,
        )

        left_inner = landmark_to_pixel(
            self.landmarks.landmark[LEFT_EYE_INNER],
            self.width,
            self.height,
        )

        right_upper = landmark_to_pixel(
            self.landmarks.landmark[RIGHT_UPPER_EYELID],
            self.width,
            self.height,
        )

        right_lower = landmark_to_pixel(
            self.landmarks.landmark[RIGHT_LOWER_EYELID],
            self.width,
            self.height,
        )

        right_outer = landmark_to_pixel(
            self.landmarks.landmark[RIGHT_EYE_OUTER],
            self.width,
            self.height,
        )

        right_inner = landmark_to_pixel(
            self.landmarks.landmark[RIGHT_EYE_INNER],
            self.width,
            self.height,
        )

        (
            self.ear,
            self.total_blinks,
        ) = self.blink_detector.detect(
            left_upper,
            left_lower,
            left_outer,
            left_inner,
            right_upper,
            right_lower,
            right_outer,
            right_inner,
        )

        self.blink_tracker.update(
            self.total_blinks
        )

        return True

    # ==========================================
    # Blink Dashboard
    # ==========================================

    def draw_blink_dashboard(self):

        cv2.putText(
            self.frame,
            f"EAR : {self.ear:.3f}",
            (20, 160),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )

        cv2.putText(
            self.frame,
            f"Blinks : {self.total_blinks}",
            (20, 190),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2,
        )    
        
    # ==========================================
    # Head Pose
    # ==========================================

    def process_head_pose(self):

        (
            self.yaw,
            self.pitch,
            self.head_direction,
            self.head_stability,
        ) = self.head_pose.estimate(
            self.landmarks,
            self.width,
            self.height,
        )

        self.head_tracker.update(
            self.head_direction
        )

        return True    
    
    # ==========================================
    # Head Pose Dashboard
    # ==========================================

    def draw_head_dashboard(self):

        stats = self.head_tracker.statistics()

        cv2.putText(
            self.frame,
            f"Head : {self.head_direction}",
            (20, 225),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            self.frame,
            f"Yaw : {self.yaw:.3f}",
            (20, 255),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            self.frame,
            f"Stability : {self.head_stability:.1f}",
            (20, 285),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 200, 0),
            2,
        )

        cv2.putText(
            self.frame,
            f"Attention : {stats['attention']:.1f}%",
            (20, 315),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )
        
    # ==========================================
    # Emotion Detection
    # ==========================================

    def process_emotion(self):

        bbox = self.face_detector.get_face_bbox(
            self.landmarks,
            self.width,
            self.height,
        )

        x, y, w, h = bbox

        face = self.frame[
            y:y + h,
            x:x + w,
        ]

        self.emotion, self.emotion_confidence = (
            self.emotion_detector.predict(face)
        )

        self.emotion_tracker.update(
            self.emotion
        )

        return True    
    
    # ==========================================
    # Emotion Dashboard
    # ==========================================

    def draw_emotion_dashboard(self):

        stats = self.emotion_tracker.statistics()

        cv2.putText(
            self.frame,
            f"Emotion : {self.emotion}",
            (20, 350),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            self.frame,
            f"Confidence : {self.emotion_confidence:.1f}%",
            (20, 380),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )

        cv2.putText(
            self.frame,
            f"Dominant : {stats['dominant_emotion']}",
            (20, 410),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 200, 0),
            2,
        )

        cv2.putText(
            self.frame,
            f"Positivity : {stats['positivity']:.1f}%",
            (20, 440),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )
        
    # ==========================================
    # Interview Analyzer
    # ==========================================

    def update_interview(self):

        # Eye Contact
        eye_stats = self.eye_tracker.statistics()

        self.analyzer.update_eye_contact(
            eye_stats["eye_contact"]
        )

        # Blink
        blink_stats = self.blink_tracker.statistics()

        self.analyzer.update_blink_rate(
            blink_stats["blink_rate"]
        )

        # Head Pose
        self.analyzer.update_head_stability(
            self.head_stability
        )

        # Emotion
        emotion_stats = self.emotion_tracker.statistics()

        self.analyzer.update_emotion(
            self.emotion,
            emotion_stats["positivity"],
        )    
        
        #live_score.update
        self.live_score.update(
            self.eye_tracker.eye_contact_percentage(),
            self.communication_score,
            self.emotion_tracker.positivity(),
            self.head_tracker.stability(),
            self.emotion,
        )
        
    # ==========================================
    # Overall Dashboard
    # ==========================================

    def draw_dashboard(self):
        
        # -------------------------
        # Dashboard Title
        # -------------------------

        cv2.putText(
            self.frame,
            "InterviewAce Dashboard",
            (20,35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,255),
            2,
        )

        self.draw_eye_dashboard()

        self.draw_blink_dashboard()

        self.draw_head_dashboard()

        self.draw_emotion_dashboard()

        report = self.analyzer.generate_report()

        cv2.putText(
            self.frame,
            f"Overall Score : {report['overall_score']:.1f}",
            (20, 430),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        fps = self.fps.get_fps()

        cv2.putText(
            self.frame,
            f"FPS : {fps}",
            (1050, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2,
        )
        #----------------------------------
        # Timer Section
        #----------------------------------
        elapsed = int(self.analyzer.duration())

        minutes = elapsed // 60

        seconds = elapsed % 60

        cv2.putText(
            self.frame,
            f"Time : {minutes:02}:{seconds:02}",
            (1000, 170),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,255),
            2,
        )
        
        # ======================================
        # Interview Progress
        # ======================================

        progress = (self.current_question + 1) / len(self.questions)

        bar_width = 220

        filled = int(bar_width * progress)

        cv2.putText(
            self.frame,
            "Interview Progress",
            (950, 210),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,255),
            2,
        )

        # Background Bar
        cv2.rectangle(
            self.frame,
            (950,230),
            (950 + bar_width,250),
            (70,70,70),
            -1,
        )

        # Filled Part
        cv2.rectangle(
            self.frame,
            (950,230),
            (950 + filled,250),
            (0,255,0),
            -1,
        )

        # Border
        cv2.rectangle(
            self.frame,
            (950,230),
            (950 + bar_width,250),
            (255,255,255),
            2,
        )

        cv2.putText(
            self.frame,
            f"{int(progress*100)}%",
            (1025,280),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,255),
            2,
        )

        # ======================================
        # Calibration Values
        # ======================================

        cv2.putText(
            self.frame,
            f"Gaze : {self.gaze_ratio:.3f}",
            (950, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            self.frame,
            f"Yaw : {self.yaw:.3f}",
            (950, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2,
        )

        cv2.putText(
            self.frame,
            f"Pitch : {self.pitch:.3f}",
            (950, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 255),
            2,
        )
        
         # Candidate Performance
         
        self.draw_live_score()
        
        self.draw_ai_feedback()
        
        
    def draw_live_score(self):

        score = self.live_score.score()

        x = 930
        y = 220

        cv2.rectangle(
        self.frame,
        (910,190),
        (1260,470),
        (40,40,40),
        -1,
        )

        cv2.rectangle(
        self.frame,
        (910,190),
        (1260,470),
        (0,255,255),
        2,
        )

        cv2.putText(
        self.frame,
        "Candidate Performance",
        (930,220),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2,
        )

        cv2.putText(
        self.frame,
        f"Confidence : {score['confidence']}%",
        (930,270),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2,
        )

        cv2.putText(
        self.frame,
        f"Eye Contact : {score['eye']:.1f}%",
        (930,310),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2,
        )

        cv2.putText(
        self.frame,
        f"Communication : {score['communication']}",
        (930,350),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2,
        )

        cv2.putText(
        self.frame,
        f"Emotion : {score['emotion']}",
        (930,390),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255,255,255),
        2,
        )    
        
        
    #draw_live_score()
    
    def draw_ai_feedback(self):

        cv2.rectangle(
        self.frame,
        (910, 490),
        (1260, 700),
        (40, 40, 40),
        -1,
        )

        cv2.rectangle(
        self.frame,
        (910, 490),
        (1260, 700),
        (0, 255, 255),
        2,
        )

        cv2.putText(
        self.frame,
        "AI Evaluation",
        (930, 520),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2,
        )

        y = 560

        for line in self.ai_feedback.split("\n"):

            cv2.putText(
            self.frame,
            line[:45],
            (925, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255,255,255),
            1,
            )

            y += 22

            if y > 680:
                break
    # ======================================
    # Draw Current Interview Question
    # ======================================
    def draw_question(self):

        if not hasattr(self, "questions"):
            return

        if self.current_question >= len(self.questions):
            return
        
        # Background
        cv2.rectangle(
            self.frame,
            (10,460),
            (1240,680),
            (45,45,45),
            -1,
        )
        
        # Border
        cv2.rectangle(
            self.frame,
            (10,460),
            (1240,680),
            (0,255,255),
            2,
        )
        
         # Title
        cv2.putText(
            self.frame,
            f"Question {self.current_question+1}/{len(self.questions)}",
            (25,495),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,255),
            2,
        )
        
        remaining = max(
            0,
            int(
                self.question_duration -
                (time.time() - self.question_start)
            )
        )

        cv2.putText(
            self.frame,
            f"Remaining : {remaining}s",
            (980,495),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,255),
            2,
            )
        
        # Question
        cv2.putText(
            self.frame,
            self.questions[self.current_question],
            (25,540),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255,255,255),
            2,
        )
    # ==========================================
    # Main Loop
    # ==========================================

    def run(self):

        print("Starting InterviewAce AI...")
        
        print("\n========== Interview Setup ==========")
        
        print("1. HR Interview")
        print("2. Technical Interview")

        choice = input("\nChoose Interview Type (1/2): ")
        
        if choice == "1":
            self.questions = self.interview.hr_interview()
        
        else:    
            print("\nAvailable Skills")
            
            print("python")
            print("machine learning")
            print("deep learning")
            print("computer vision")
            print("sql")
            
            skill = input("\nEnter Skill : ").lower()
            
            self.questions = self.interview.technical_interview(skill)
            
        print("\nInterview Questions Loaded.")
        
        for i, q in enumerate(self.questions, 1):
            
            print(f"{i}. {q}")
 
        print("=" * 40)
        
        self.current_question = 0
        self.question_duration = 30
        self.question_start = time.time()
        
        # AI welcomes the candidate
        self.voice.speak("Welcome to Interview Ace AI.")
        
        self.voice.speak("Your interview is starting now.")
        
        self.speech.start()
        
        # Speak first question
        self.voice.speak(
            f"Question 1. {self.questions[0]}"
        )
        
        while True:

            # -------------------------
            # Read Camera
            # -------------------------
            if not self.read_frame():
                break

            # -------------------------
            # Face Detection
            # -------------------------
            if self.process_face():

                # Iris
                self.process_iris()

                # Gaze
                self.process_gaze()

                # Eye Contact
                self.process_eye_contact()

                # Blink
                self.process_blink()

                # Head Pose
                self.process_head_pose()

                # Emotion
                self.process_emotion()

                # Interview Analysis
                self.update_interview()

                # Dashboard
                self.draw_dashboard()
                
                self.draw_question()
                
                if time.time() - self.question_start >= self.question_duration:
                    
                    answer = self.speech.get_transcript()

                    result = self.evaluator.evaluate(
                        self.questions[self.current_question],
                        answer,
                    )
                    
                    self.ai_feedback = result

                    print("\n==========================")
                    print(result)
                    print("==========================\n")
                    
                    self.current_question += 1

                    self.question_start = time.time()

                    if self.current_question >= len(self.questions):
                        break
                    
                    self.voice.speak(
                        f"Question {self.current_question + 1}. "
                        f"{self.questions[self.current_question]}"
                    )

            else:

                cv2.putText(
                    self.frame,
                    "Face Not Detected",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 0, 255),
                    2,
                )

            # Show Frame
            cv2.imshow(
                "InterviewAce AI",
                self.frame,
            )

            key = cv2.waitKey(1) & 0xFF
            
            # Next Question
            if key == ord("n"):
                if self.current_question < len(self.questions) - 1:
                    
                    self.current_question += 1
                    
                    self.question_start = time.time()
                    
                    self.voice.speak(
                        f"Question {self.current_question + 1}. "
                        f"{self.questions[self.current_question]}"
                    )     

            # Quit
            if key == ord("q"):
                break

        # Cleanup AFTER loop exits
        self.cleanup()
        
    # ==========================================
    # Cleanup
    # ==========================================

    def cleanup(self):

        print("\nClosing InterviewAce AI...")

        self.camera.release()

        cv2.destroyAllWindows()

        print("Interview Session Finished.")
        
        # -------------------------
        # Speech Analysis
        # -------------------------

        audio_file = self.speech.stop()

        if audio_file:

            self.speech_result = self.speech_ai.analyze(
            audio_file,
            self.analyzer.duration(),
        )
        
        if self.speech_result:
            self.communication_score = self.communication.communication_score(
                self.speech_result["wpm"],
                self.speech_result["fillers"],
            )    
            self.communication_feedback = self.communication.feedback(
                self.speech_result["wpm"],
                self.speech_result["fillers"],
            )
                
        report = self.analyzer.generate_report()
        
        self.pdf.generate(
            "Interview_Report.pdf",
            report,
            self.ai_feedback,
        )
        
        self.history.save(
        self.interview_type,
        report,
        )

        print("\n========== FINAL REPORT ==========")

        print(f"Duration          : {report['duration']} sec")
        print(f"Eye Contact       : {report['eye_contact']} %")
        print(f"Blink Rate        : {report['blink_rate']} blinks/min")
        print(f"Head Stability    : {report['head_stability']} %")
        print(f"Emotion           : {report['emotion']}")
        print(f"Positivity        : {report['positivity']} %")
        print(f"Overall Score     : {report['overall_score']}")
        
        if self.speech_result:

            print(f"WPM               : {self.speech_result['wpm']}")
            print(f"Filler Words      : {self.speech_result['fillers']}")
            print(f"Transcript        : {self.speech_result['text']}")
        
        print(f"Communication Score : {self.communication_score}")
        
        print("\nFeedback:")

        for item in report["feedback"]:
            print(f" - {item}")

        if self.communication_feedback:

            print("\nCommunication Feedback:")

        for item in self.communication_feedback:
            print(f" - {item}")

        print("==================================")
            