import pdfplumber
import fitz
import re


class ResumeParser:

    def extract_text(self, pdf_path):

        text = ""

        try:
            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text + "\n"

        except Exception:
            pass

        if len(text.strip()) == 0:

            doc = fitz.open(pdf_path)

            for page in doc:
                text += page.get_text()

            doc.close()

        return text

    def parse_resume(self, text):

        lines = [
            x.strip()
            for x in text.split("\n")
            if x.strip()
        ]

        name = lines[0] if lines else "Unknown"

        skills = []

        projects = []

        education = []

        experience = []

        skill_keywords = [

            "python",
            "java",
            "c++",
            "sql",
            "react",
            "fastapi",
            "flask",
            "opencv",
            "tensorflow",
            "pytorch",
            "machine learning",
            "deep learning",
            "docker",
            "mongodb",
            "mysql",
            "javascript",
            "typescript",
            "node",
            "git",
            "linux"

        ]

        for line in lines:

            lower = line.lower()

            for skill in skill_keywords:

                if skill in lower:

                    if skill.title() not in skills:
                        skills.append(skill.title())

            if "project" in lower:

                continue

            if (
                "interviewace" in lower
                or "emotion" in lower
                or "music system" in lower
                or "website blocker" in lower
            ):

                projects.append(line)

            if (
                "b.tech" in lower
                or "bachelor" in lower
                or "university" in lower
                or "college" in lower
            ):

                education.append(line)

            if (
                "intern" in lower
                or "experience" in lower
            ):

                experience.append(line)

        return {

            "name": name,

            "skills": list(set(skills)),

            "projects": projects,

            "education": education,

            "experience": experience,

        }