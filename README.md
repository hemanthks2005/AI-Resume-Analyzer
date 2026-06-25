# 🚀 AI Resume Analyzer

A modern AI-powered Resume Analyzer built using Flask and Python that helps job seekers evaluate their resumes through ATS scoring, skill matching, resume analytics, and intelligent improvement suggestions.

---

Live Application : https://ai-resume-analyzer-bz2v.onrender.com

GitHub Repository: https://github.com/hemanthks2005/AI-Resume-Analyzer


## ✨ Features

### 📄 Resume Parsing

* Upload PDF resumes
* Extract resume content automatically
* Fast and accurate text extraction using pdfplumber

### 🎯 ATS Score Calculation

* Analyze resume against job descriptions
* Calculate ATS compatibility score
* Identify matching and missing skills

### 🤖 AI Suggestions

* Generate resume improvement recommendations
* Highlight missing technologies and keywords
* Improve chances of getting shortlisted

### 📊 Resume Analytics Dashboard

* Word Count Analysis
* Character Count Analysis
* Skills Detected
* Education Detection
* Experience Detection
* Project Detection

### 🗄️ Database Integration

* SQLite database storage
* Resume analysis history
* ATS score tracking

### 📥 PDF Report Generation

* Download analysis reports
* Share results easily
* Professional report format

---

## 🛠️ Tech Stack

| Technology | Usage                   |
| ---------- | ----------------------- |
| Python     | Backend Logic           |
| Flask      | Web Framework           |
| SQLite     | Database                |
| PDFPlumber | PDF Parsing             |
| ReportLab  | PDF Report Generation   |
| HTML5      | Frontend                |
| CSS3       | Styling                 |
| JavaScript | Client-side Interaction |

---

## 🏗️ Project Architecture

```text
Resume-Analyzer
│
├── app.py
├── requirements.txt
├── templates
│   ├── index.html
│   ├── resume_text.html
│   ├── history.html
│   └── success.html
│
├── utils
│   ├── pdf_extractor.py
│   ├── skill_detector.py
│   ├── ats_calculator.py
│   ├── resume_analytics.py
│   ├── suggestions.py
│   └── database.py
│
├── uploads
└── resume_analyzer.db
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/hemanthks2005/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

---

## 🎯 How It Works

1. Upload Resume PDF
2. Paste Job Description
3. Resume Text Extraction
4. Skill Detection
5. ATS Score Calculation
6. Missing Skill Analysis
7. Resume Analytics Generation
8. AI Suggestions Creation
9. Save Results to Database
10. Download Analysis Report

---

## 📈 Current Features Completed

* ✅ PDF Upload
* ✅ Resume Parsing
* ✅ ATS Score Engine
* ✅ Skill Detection
* ✅ Job Description Matching
* ✅ Missing Skills Analysis
* ✅ AI Suggestions
* ✅ Resume Analytics
* ✅ SQLite Database
* ✅ Resume History
* ✅ PDF Report Download
* ✅ Modern Dashboard UI

---

## 🚀 Future Enhancements

* User Authentication
* AI Chat Assistant
* Resume Ranking System
* Multiple Resume Comparison
* Cloud Deployment
* OpenAI Integration
* Resume Template Generator

---

## 👨‍💻 Author

**Hemanth K S**

Aspiring Software Developer passionate about Python, Flask, AI Applications, and Full Stack Development.

---

⭐ If you like this project, consider giving it a star on GitHub.
