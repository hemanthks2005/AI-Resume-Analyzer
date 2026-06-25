# utils/ats_calculator.py

def calculate_ats_score(resume_skills, job_skills):

    matched = 0

    for skill in job_skills:
        if skill in resume_skills:
            matched += 1

    if len(job_skills) == 0:
        return 0, []

    score = (matched / len(job_skills)) * 100

    missing_skills = []

    for skill in job_skills:
        if skill not in resume_skills:
            missing_skills.append(skill)

    return round(score), missing_skills