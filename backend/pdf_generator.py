from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(data, file_path):

    doc = SimpleDocTemplate(file_path)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI CAREER AGENT REPORT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # Candidate

    content.append(
        Paragraph(
            "<b>Candidate Information</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Name: {data['candidate_name']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Email: {data['candidate_email']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Role: {data['role']}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    # ATS

    content.append(
        Paragraph(
            "<b>ATS Analysis</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"ATS Score: {data['ats_score']}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Matched Skills:",
            styles["BodyText"]
        )
    )

    for skill in data["matching_skills"]:
        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(
        Paragraph(
            "Missing Skills:",
            styles["BodyText"]
        )
    )

    for skill in data["missing_skills"]:
        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 15))

    # Hiring

    content.append(
        Paragraph(
            "<b>Recruitment Decision</b>",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"Recommendation: {data['recommendation']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Confidence: {data['confidence']}%",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Assessment: {data['assessment']}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"Action: {data['action']}",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # Roadmap

    content.append(
        Paragraph(
            "<b>Learning Roadmap</b>",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            str(data["roadmap"]),
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    # Interview

    content.append(
        Paragraph(
            "<b>Interview Plan</b>",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            str(data["interview"]),
            styles["BodyText"]
        )
    )

    doc.build(content)

    return file_path