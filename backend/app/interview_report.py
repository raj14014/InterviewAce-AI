class InterviewReport:

    def __init__(self):
        pass

    def generate(
        self,
        analyzer,
        evaluation,
    ):

        report = analyzer.generate_report()

        return f"""
==============================

Interview Report

Overall Score : {report['overall_score']:.1f}/100

Eye Contact : {report['eye_contact']:.1f}%

Blink Rate : {report['blink_rate']:.1f}

Emotion : {report['emotion']}

Communication Score : {report['communication_score']}

--------------------------------

AI Evaluation

{evaluation}

==============================
"""