from flask import Flask, render_template, request
import os
from utils.pdf_extractor import extract_text_from_pdf
from utils.skill_detector import detect_skills, extract_job_skills
from utils.ats_calculator import calculate_ats_score
from utils.suggestions import generate_suggestions
from utils.resume_analytics import analyze_resume
from utils.section_detector import detect_sections
from utils.pdf_report import generate_pdf_report
from flask import send_file
from utils.database import (
    create_database,
    save_resume_analysis,
    get_all_resumes,
    get_statistics
)

JOB_SKILLS = [
    "Python",
    "Flask",
    "SQL",
    "Git"
]

app = Flask(__name__)
create_database()

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():

    if "resume" not in request.files:
        return "No file selected"

    file = request.files["resume"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    resume_text = extract_text_from_pdf(filepath)
    sections = detect_sections(resume_text)
    detected_skills = detect_skills(resume_text)

    job_description = request.form.get("job_description", "")

    job_skills = extract_job_skills(job_description)

    ats_score, missing_skills = calculate_ats_score(
    detected_skills,
    job_skills
    )
    save_resume_analysis(
    file.filename,
    ats_score,
    detected_skills,
    missing_skills
    )
    suggestions = generate_suggestions(
    missing_skills
    )
    analytics = analyze_resume(
    resume_text,
    detected_skills
    )
    pdf_report = generate_pdf_report(
    file.filename,
    ats_score,
    detected_skills,
    missing_skills,
    suggestions
    )

    return render_template(
    "resume_text.html",
    filename=file.filename,
    text=resume_text,
    skills=detected_skills,
    ats_score=ats_score,
    missing_skills=missing_skills,
    job_skills=job_skills,
    suggestions=suggestions,
    analytics=analytics,
    sections=sections,
    pdf_report=pdf_report
    )

@app.route("/download/<filename>")
def download_report(filename):

    report_path = (
        f"uploads/{filename}_ATS_Report.pdf"
    )

    return send_file(
        report_path,
        as_attachment=True
    )

@app.route("/history")
def history():

    resumes = get_all_resumes()

    stats = get_statistics()

    return render_template(
        "history.html",
        resumes=resumes,
        stats=stats
    )
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)