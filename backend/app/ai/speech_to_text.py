import whisper


class SpeechToText:

    def __init__(self):
        print("Loading Whisper Model...")
        self.model = whisper.load_model("base")
        print("Whisper Ready.")

    def transcribe(self, audio_path):

        result = self.model.transcribe(audio_path)

        return result["text"]