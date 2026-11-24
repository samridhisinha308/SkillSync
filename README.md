# SkillSync – Resume Analysis & Job Matching Platform

SkillSync is a Python-based web application that analyzes resumes, extracts technical skills, and evaluates how well a candidate's profile matches a given job description.

It helps users identify skill gaps, understand job requirements, and receive personalized recommendations to improve their career readiness.

## 🚀 Features

- **Resume Parsing:** Upload and extract text from PDF resumes.
- **Skill Extraction:** Automatically identify technical skills from resumes.
- **Job Matching:** Compare resumes with job descriptions using TF-IDF and Cosine Similarity.
- **Match Score:** Calculate an estimated resume-job compatibility score.
- **Skill Gap Analysis:** Identify matched and missing required and preferred skills.
- **Skill Coverage:** Analyze skill coverage using weighted scoring.
- **Personalized Recommendations:** Get suggestions to improve missing skills.
- **PDF Report:** Download a detailed analysis report.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| Streamlit | Web application interface |
| Scikit-learn | TF-IDF and Cosine Similarity |
| PyPDF2 | PDF text extraction |
| Pandas & NumPy | Data processing |
| ReportLab | PDF report generation |

## ⚙️ How It Works

1. Upload your resume in PDF format.
2. SkillSync extracts text and identifies technical skills.
3. Enter a job description.
4. The application calculates a matching score.
5. View matched skills, missing skills, and skill coverage.
6. Get personalized recommendations and download your PDF report.

## 💻 Installation & Setup

**1. Clone the repository**

```bash
git clone https://github.com/samridhisinha308/SkillSync.git
```

**2. Navigate to the project directory**

```bash
cd SkillSync
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
streamlit run app.py
```

## 📁 Project Structure

```text
SkillSync/
│
├── .streamlit/
│   └── config.toml
│
├── utils/
│   ├── job_matcher.py
│   ├── resume_parser.py
│   └── skill_extractor.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔮 Future Scope

- Integration with live job portals and job listings.
- Advanced NLP-based skill extraction.
- Resume improvement suggestions.
- Personalized learning roadmaps.
- Support for multiple resume formats.

## 👩‍💻 Author

**Samridhi Sinha**

B.Tech CSE (AI & ML)

[GitHub](https://github.com/samridhisinha308)

---

*SkillSync – Your Resume. Your Skills. Your Next Opportunity.*