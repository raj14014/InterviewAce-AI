from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import getSampleStyleSheet


class PDFReport:

    def __init__(self):
        self.styles = getSampleStyleSheet()

    def generate(
        self,
        filename,
        report,
        evaluation,
    ):

        doc = SimpleDocTemplate(filename)

        story = []

        style = self.styles["Heading1"]

        story.append(
            Paragraph(
                "InterviewAce AI Report",
                style,
            )
        )

        story.append(Spacer(1,20))

        style = self.styles["BodyText"]

        story.append(
            Paragraph(
                f"Overall Score : {report['overall_score']:.1f}",
                style,
            )
        )

        story.append(
            Paragraph(
                f"Eye Contact : {report['eye_contact']:.1f}%",
                style,
            )
        )

        story.append(
            Paragraph(
                f"Blink Rate : {report['blink_rate']:.1f}",
                style,
            )
        )

        story.append(
            Paragraph(
                f"Head Stability : {report['head_stability']:.1f}%",
                style,
            )
        )

        story.append(
            Paragraph(
                f"Emotion : {report['emotion']}",
                style,
            )
        )

        story.append(Spacer(1,20))

        story.append(
            Paragraph(
                "<b>AI Evaluation</b>",
                style,
            )
        )

        story.append(
            Paragraph(
                evaluation.replace("\n","<br/>"),
                style,
            )
        )

        doc.build(story)

        print("PDF Report Saved :", filename)