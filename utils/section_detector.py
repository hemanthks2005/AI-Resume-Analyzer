def detect_sections(text):

    text = text.lower()

    sections = {
        "Education": False,
        "Skills": False,
        "Projects": False,
        "Experience": False,
        "Certifications": False
    }

    if "education" in text:
        sections["Education"] = True

    if "skills" in text:
        sections["Skills"] = True

    if "project" in text:
        sections["Projects"] = True

    if "experience" in text:
        sections["Experience"] = True

    if "certification" in text or "certifications" in text:
        sections["Certifications"] = True

    return sections