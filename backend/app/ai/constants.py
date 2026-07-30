"""
InterviewAce AI
Shared Constants
"""

# ==========================================
# Camera
# ==========================================

CAMERA_ID = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

FPS = 30


# ==========================================
# MediaPipe Face Mesh
# ==========================================

MAX_NUM_FACES = 1

MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5


# ==========================================
# Iris Landmarks
# ==========================================

LEFT_IRIS = [469, 470, 471, 472]
RIGHT_IRIS = [474, 475, 476, 477]


# ==========================================
# Left Eye Landmarks
# ==========================================

LEFT_EYE_OUTER = 33
LEFT_EYE_INNER = 133

LEFT_UPPER_EYELID = 159
LEFT_LOWER_EYELID = 145


# ==========================================
# Right Eye Landmarks
# ==========================================

RIGHT_EYE_OUTER = 263
RIGHT_EYE_INNER = 362

RIGHT_UPPER_EYELID = 386
RIGHT_LOWER_EYELID = 374


# ==========================================
# Head Pose Landmarks
# ==========================================

NOSE_TIP = 1
CHIN = 152

LEFT_FACE = 234
RIGHT_FACE = 454

LEFT_EYE = 33
RIGHT_EYE = 263


# ==========================================
# Eye Contact Thresholds
# ==========================================

LOOKING_LEFT_THRESHOLD = 0.40
LOOKING_RIGHT_THRESHOLD = 0.60

PERFECT_CONTACT_MIN = 0.45
PERFECT_CONTACT_MAX = 0.55


# ==========================================
# Blink Threshold
# ==========================================

EAR_THRESHOLD = 0.24
EAR_CONSECUTIVE_FRAMES = 3


# ==========================================
# Drawing Colors (BGR)
# ==========================================

GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
WHITE = (255, 255, 255)
ORANGE = (0, 165, 255)
PURPLE = (255, 0, 255)


# ==========================================
# Font
# ==========================================

FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
THICKNESS = 2