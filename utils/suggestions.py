def generate_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:
        suggestions.append(
            f"Consider adding experience or projects related to {skill}."
        )

    suggestions.append(
        "Include measurable achievements in your projects."
    )

    suggestions.append(
        "Add your GitHub profile link."
    )

    suggestions.append(
        "Highlight technical projects clearly."
    )

    return suggestions