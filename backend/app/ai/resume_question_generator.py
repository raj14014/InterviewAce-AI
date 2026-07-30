class ResumeQuestionGenerator:

    def generate(self, resume):

        questions = []

        name = resume.get("name", "")
        skills = resume.get("skills", [])
        projects = resume.get("projects", [])

        questions.append(
            f"Tell me about yourself {name}."
        )

        for skill in skills[:3]:

            questions.append(
                f"What is your experience with {skill}?"
            )

        for project in projects[:2]:

            questions.append(
                f"Explain your project {project}."
            )

        questions.append(
            "Why should we hire you?"
        )

        return questions