class LiveScore:

    def __init__(self):

        self.confidence = 0
        self.communication = 0
        self.eye = 0
        self.emotion = "Neutral"

    def update(
        self,
        eye,
        communication,
        positivity,
        head,
        emotion,
    ):

        self.eye = eye
        self.communication = communication
        self.emotion = emotion

        self.confidence = round(
            eye*0.35 +
            communication*0.30 +
            positivity*0.20 +
            head*0.15,
            1
        )

    def score(self):
        return {
            "confidence": self.confidence,
            "eye": self.eye,
            "communication": self.communication,
            "emotion": self.emotion,
        }