"""
InterviewAce AI
AI Voice Interviewer
"""

import pyttsx3


class VoiceInterviewer:

    def __init__(self):

        self.engine = pyttsx3.init()

        # Speaking speed
        self.engine.setProperty("rate", 170)

        # Volume (0.0 - 1.0)
        self.engine.setProperty("volume", 1.0)

    def speak(self, text):

        print(f"🔊 {text}")      # Debug

        self.engine.stop()       # Clear previous queue

        self.engine.say(text)

        self.engine.runAndWait()