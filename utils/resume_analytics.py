def analyze_resume(text, skills):

    words = len(text.split())

    characters = len(text)

    projects = text.lower().count("project")

    education = (
        "yes"
        if any(
            word in text.lower()
            for word in [
                "education",
                "b.e",
                "btech",
                "degree",
                "university"
            ]
        )
        else "no"
    )

    experience = (
        "yes"
        if any(
            word in text.lower()
            for word in [
                "experience",
                "internship",
                "work"
            ]
        )
        else "no"
    )

    return {
        "words": words,
        "characters": characters,
        "skills_count": len(skills),
        "projects": projects,
        "education": education,
        "experience": experience
    }