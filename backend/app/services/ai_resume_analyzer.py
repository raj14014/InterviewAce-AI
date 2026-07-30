import re


class AIResumeAnalyzer:

    @staticmethod
    def extract_skills(text: str):

        skills_database = [
            "python",
            "java",
            "c++",
            "c",
            "javascript",
            "typescript",
            "react",
            "node",
            "fastapi",
            "flask",
            "django",
            "tensorflow",
            "pytorch",
            "opencv",
            "mediapipe",
            "mongodb",
            "mysql",
            "sql",
            "docker",
            "git",
            "github",
            "machine learning",
            "deep learning",
            "computer vision",
            "nlp",
            "aws",
            "azure"
        ]

        found_skills = []

        text = text.lower()

        for skill in skills_database:
            if skill in text:
                found_skills.append(skill.title())

        return list(set(found_skills))

    @staticmethod
    def resume_score(skills):

        score = min(len(skills) * 4, 100)

        return score

    @staticmethod
    def suggestions(score):

        tips = []

        if score < 40:
            tips.append("Add more technical skills.")
            tips.append("Include projects.")
            tips.append("Mention certifications.")

        elif score < 70:
            tips.append("Improve project descriptions.")
            tips.append("Add GitHub profile.")
            tips.append("Include internships.")

        else:
            tips.append("Excellent Resume.")
            tips.append("Ready for Interviews.")

        return tips