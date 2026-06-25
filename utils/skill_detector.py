SKILLS = [
    "python",
    "java",
    "sql",
    "mysql",
    "flask",
    "django",
    "react",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "machine learning",
    "data structures",
    "c",
    "c++"
]

def detect_skills(text):

    detected = []

    text = text.lower()

    for skill in SKILLS:
        if skill.lower() in text:
            detected.append(skill.title())

    return detected


def extract_job_skills(job_description):

    found_skills = []

    job_description = job_description.lower()

    for skill in SKILLS:
        if skill.lower() in job_description:
            found_skills.append(skill.title())

    return found_skills