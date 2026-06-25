import sqlite3

def create_database():

    conn = sqlite3.connect("resume_analyzer.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        ats_score INTEGER,
        skills TEXT,
        missing_skills TEXT
    )
    """)

    conn.commit()
    conn.close()

import sqlite3

def save_resume_analysis(
    filename,
    ats_score,
    skills,
    missing_skills
):

    conn = sqlite3.connect("resume_analyzer.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO resumes
        (filename, ats_score, skills, missing_skills)
        VALUES (?, ?, ?, ?)
        """,
        (
            filename,
            ats_score,
            ", ".join(skills),
            ", ".join(missing_skills)
        )
    )

    conn.commit()
    conn.close()


def get_all_resumes():

    conn = sqlite3.connect("resume_analyzer.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM resumes ORDER BY id DESC"
    )

    data = cursor.fetchall()

    conn.close()

    return data

def get_statistics():

    conn = sqlite3.connect("resume_analyzer.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
        COUNT(*),
        AVG(ats_score),
        MAX(ats_score),
        MIN(ats_score)
        FROM resumes
        """
    )

    stats = cursor.fetchone()

    conn.close()

    return stats