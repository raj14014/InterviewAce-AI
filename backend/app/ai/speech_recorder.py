"""
InterviewAce AI
Speech Recorder
"""

import sounddevice as sd
import soundfile as sf
import threading


class SpeechRecorder:

    def __init__(self):

        self.sample_rate = 16000

        self.channels = 1

        self.recording = False

        self.audio = []

    # -------------------------
    # Callback
    # -------------------------

    def callback(self, indata, frames, time, status):

        if self.recording:
            self.audio.append(indata.copy())

    # -------------------------
    # Start Recording
    # -------------------------

    def start(self):

        if self.recording:
            return

        self.audio = []

        self.recording = True

        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=self.channels,
            callback=self.callback,
        )

        self.stream.start()

        print("🎤 Recording Started")

    # -------------------------
    # Stop Recording
    # -------------------------

    def stop(self, filename="interview_audio.wav"):

        if not self.recording:
            return None

        self.recording = False

        self.stream.stop()

        self.stream.close()

        if len(self.audio) == 0:
            return None

        import numpy as np

        audio = np.concatenate(self.audio, axis=0)

        sf.write(
            filename,
            audio,
            self.sample_rate,
        )

        print("✅ Recording Saved")

        return filename