from transformers import pipeline


class AnswerEvaluator:

    def __init__(self):

        print("Loading AI Evaluator...")

        self.model = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
        )

        print("AI Evaluator Ready.")

    def evaluate(
        self,
        question,
        answer,
    ):

        prompt = f"""
You are an HR interviewer.

Question:
{question}

Candidate Answer:
{answer}

Return ONLY in this format.

Overall Score: <0-100>

Strengths:
- point1
- point2

Weaknesses:
- point1
- point2

Placement Ready:
Yes or No

Recommendation:
Short recommendation.
"""

        output = self.model(
            prompt,
            max_new_tokens=200,
        )

        return output[0]["generated_text"]