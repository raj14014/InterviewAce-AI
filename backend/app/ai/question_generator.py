"""
InterviewAce AI
AI Interview Question Generator
"""

import random

class QuestionGenerator:

    def __init__(self):

        self.hr_questions = [
            "Tell me about yourself.",
            "Why should we hire you?",
            "What are your strengths?",
            "What are your weaknesses?",
            "Why do you want to join our company?",
            "Where do you see yourself in 5 years?",
            "Describe a challenge you faced.",
            "Tell me about a project you are proud of.",
            "Why should we select you over other candidates?",
            "How do you handle pressure?"
        ]

        self.technical_questions = {

            "python": [
                "What is the difference between List and Tuple?",
                "Explain OOP in Python.",
                "What are decorators?",
                "Explain generators.",
                "Difference between multithreading and multiprocessing?"
            ],

            "machine learning": [
                "What is overfitting?",
                "Difference between supervised and unsupervised learning?",
                "Explain bias-variance tradeoff.",
                "What is cross validation?",
                "What is gradient descent?"
            ],

            "deep learning": [
                "Explain CNN.",
                "Difference between CNN and RNN.",
                "What is backpropagation?",
                "Explain dropout.",
                "Why ReLU is preferred?"
            ],

            "computer vision": [
                "Explain image classification.",
                "Difference between detection and segmentation.",
                "What is YOLO?",
                "Explain OpenCV.",
                "What is object detection?"
            ],

            "sql": [
                "Difference between DELETE, DROP and TRUNCATE.",
                "Explain JOIN.",
                "What is normalization?",
                "Primary Key vs Foreign Key.",
                "What are indexes?"
            ]
        }
        
    # ---------------------------------
    # HR Questions
    # ---------------------------------

    def generate_hr_questions(
        self,
        count=5,
    ):

        return random.sample(
            self.hr_questions,
            min(count, len(self.hr_questions))
    )
        
    # ---------------------------------
    # Technical Questions
    # --------------------------------- 
    def generate_technical_questions(
        self,
        skill,
        count=5,
    ):   
        skill = skill.lower()

        if skill not in self.technical_questions:
            return []

        return random.sample(
            self.technical_questions[skill],
            min(
                count,
                len(self.technical_questions[skill])
            )
        )