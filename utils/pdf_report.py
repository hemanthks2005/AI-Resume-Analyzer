from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
        filename,
        ats_score,
        skills,
        missing_skills,
        suggestions):

    pdf_file = f"uploads/{filename}_ATS_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("AI Resume Analyzer Report",
                  styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"ATS Score: {ats_score}%",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Detected Skills: {', '.join(skills)}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Missing Skills: {', '.join(missing_skills)}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "Suggestions:",
            styles["Heading2"]
        )
    )

    for suggestion in suggestions:
        content.append(
            Paragraph(
                f"• {suggestion}",
                styles["BodyText"]
            )
        )

    doc.build(content)

    return pdf_file