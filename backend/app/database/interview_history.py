import sqlite3
from datetime import datetime


class InterviewHistory:

    def __init__(self):

        self.conn = sqlite3.connect("interview_history.db")

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            date TEXT,

            question TEXT,

            answer TEXT,

            evaluation TEXT,

            words INTEGER,

            wpm INTEGER,

            fillers INTEGER,

            pauses INTEGER,

            confidence INTEGER,

            rating TEXT

        )
        """)

        self.conn.commit()

    def save(
        self,
        question,
        answer,
        result,
    ):

        voice = result["voice"]

        self.cursor.execute(
            """
            INSERT INTO interviews(

                date,

                question,

                answer,

                evaluation,

                words,

                wpm,

                fillers,

                pauses,

                confidence,

                rating

            )

            VALUES(?,?,?,?,?,?,?,?,?,?)
            """,

            (

                datetime.now().strftime("%Y-%m-%d %H:%M"),

                question,

                answer,

                result["evaluation"],

                voice["words"],

                voice["wpm"],

                voice["fillers"],

                voice["pauses"],

                voice["confidence_score"],

                voice["rating"],

            ),

        )

        self.conn.commit()

        print("Interview Saved.")
    def get_all(self):

        self.cursor.execute(
        """
        SELECT
            id,
            date,
            question,
            score,
            confidence,
            communication,
            emotion
        FROM interviews
        ORDER BY id DESC
        """
    )

        rows = self.cursor.fetchall()

        result = []

        for row in rows:

           result.append({

            "id": row[0],

            "date": row[1],

            "question": row[2],

            "score": row[3],

            "confidence": row[4],

            "communication": row[5],

            "emotion": row[6],

        })

        return result