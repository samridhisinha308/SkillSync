import streamlit as st 
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
def generate_report(score, coverage, required_skills,
                    matched_required, matched_preferred,
                    missing_skills):

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, 800, "SkillSync - Analysis Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 760, f"Overall Match Score: {score}%")
    pdf.drawString(50, 735, f"Skill Coverage: {coverage:.1f}%")
    pdf.drawString(50, 710, f"Required Skills: {len(required_skills)}")

    y = 660

    sections = [
        ("Matched Required Skills", matched_required),
        ("Matched Preferred Skills", matched_preferred),
        ("Missing Skills", missing_skills)
    ]

    for heading, skills in sections:
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(50, y, heading)
        y -= 25

        pdf.setFont("Helvetica", 11)

        for skill in skills:
            if y < 60:
                pdf.showPage()
                y = 800
                pdf.setFont("Helvetica", 11)

            pdf.drawString(65, y, f"- {skill}")
            y -= 20

        y -= 15

    pdf.save()
    buffer.seek(0)

    return buffer
st.markdown("""
<style>

/* Main application */
.stApp {
    background-color: #101426;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #191F38;
    border-right: 1px solid #303858;
}

/* Main headings */
h1, h2, h3 {
    color: #F2F3FA !important;
    font-weight: 700;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #7657E8, #4D9DE0);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton > button:hover {
    border: 1px solid #A18BFF;
    color: white;
}

/* Input fields */
.stTextArea textarea,
.stTextInput input {
    background-color: #191F38;
    color: #F2F3FA;
    border: 1px solid #384365;
    border-radius: 10px;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #191F38;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #303858;
}

/* Dividers */
hr {
    border-color: #303858;
}

</style>
""", unsafe_allow_html=True)
st.markdown(
            "<p style='text-align:center; color:#AFA6E8; "
            "font-size:17px;'>"
            "Your Resume. Your Skills. Your Next Opportunity."
            "</p>",
            unsafe_allow_html=True
        )
st.markdown("### Explore SkillSync")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📄 Resume Analysis\n\nExtract and understand your skills.")
with col2:
    st.info("🎯 Job Matching\n\nCheck your compatibility with a job.")
with col3:
    st.info("💡 Recommendations\n\nDiscover skills you need to improve.")
from utils.resume_parser import extract_resume_text
from utils.skill_extractor import extract_skills
from utils.job_matcher import calculate_match
from utils.skill_extractor import extract_priority_skills
#Page Configuration
st.set_page_config(
    page_title="SkillSync AI",
    page_icon="🎯",
    layout="wide"
)
#Main Heading
st.title("🎯 SkillSync AI")
st.subheader("Your Resume. Your Skills. Your Next Opportunity.")
st.write("An AI-powered platform to analyze resumes ,"
         "Match job descriptions and identify skill gaps .")
st.divider()
#Sidebar
st.sidebar.title("SkillSync AI")
st.sidebar.write("Navigate through the platform")
page = st.sidebar.radio("Select a section",
                        ["Home","Resume Analysis","Job Matching","About"])

# Home Page
if page == "Home":


    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #25204B, #252F58);
        padding: 45px 35px;
        border-radius: 18px;
        border: 1px solid #494078;
        margin-bottom: 30px;
    ">
        <h1 style="color: white; font-size: 38px;">
            Welcome to SkillSync AI
        </h1>
        <p style="color: #C7C9E8; font-size: 18px;">
            Bridge the gap between your skills and your dream career.
        </p>
        <p style="color: #AFA8F5; font-size: 14px;">
            AI-Powered Resume Analysis & Job Matching Platform
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("What can SkillSync do for you?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 📄 Resume Analysis
        Extract skills and analyze your resume
        to understand your professional profile.
        """)

    with col2:
        st.markdown("""
        ### 🎯 Smart Job Matching
        Compare your resume with job descriptions
        and identify skill gaps.
        """)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        ### 📊 Skill Gap Analysis
        Discover missing skills and understand
        what you need to improve.
        """)

    with col4:
        st.markdown("""
        ### 💡 Personalized Recommendations
        Get suggestions to improve your
        job readiness.
        """)

    st.divider()

    st.subheader("How It Works")

    st.markdown("""
    **01 — Upload Resume**

    Upload your PDF resume.

    **02 — Add Job Description**

    Paste the job description you want to target.

    **03 — Analyze & Improve**

    Get your match score, skill gaps and
    personalized recommendations.
    """)

    st.divider()

    st.info(
        "Your next opportunity starts with understanding your skills."
    )
# Resume Analysis Page
elif page == "Resume Analysis":
    st.markdown("""
    <div style="
        background: linear-gradient(120deg, #25204B, #252F58);
        padding: 30px;
        border-radius: 16px;
        border: 1px solid #494078;
        margin-bottom: 25px;
    ">
        <h1 style="color: white;">
            Resume Analysis
        </h1>
        <p style="color: #C7C9E8; font-size: 16px;">
            Discover your strengths, extract your skills
            and understand your professional profile.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Upload Your Resume")

    st.caption(
        "Upload your resume in PDF format to begin your analysis."
    )

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )
    if uploaded_file:
        st.success("Resume uploaded successfully!")
        st.write("File Name:", uploaded_file.name)
        with st.spinner("Extracting resume text..."):
            resume_text=extract_resume_text(uploaded_file)
            st.session_state["resume_text"]=resume_text
        if resume_text.strip():
            st.subheader("Extracted Resume Content")
            st.text_area(
                "Resume Text",
                value=resume_text,
                height=300
            )

        # Extract technical skills
        detected_skills = extract_skills(resume_text)
        st.divider()
        st.subheader("Your Resume Insights")
        st.subheader("Detected Skills")

        if detected_skills:

            total_skills = sum(
                len(skills)
                for skills in detected_skills.values()
            )
            st.markdown("### Skills Overview")
            st.metric("Total Skills Found", total_skills)

            for category, skills in detected_skills.items():

                with st.container(border=True):
                    st.markdown(f"**{category}**")
                    st.write(" · ".join(skills))

        else:
            st.info("No predefined technical skills detected.")

    else:
        st.warning("No Readable Text Found"
                       "This PDF may contain scanned images")

# Job Matching Page


elif page == "Job Matching":

    st.markdown("""
        <div style="
            background: linear-gradient(120deg, #25204B, #252F58);
            padding: 30px;
            border-radius: 16px;
            border: 1px solid #494078;
            margin-bottom: 25px;
        ">
            <h1 style="color: white;">Smart Job Matching</h1>
            <p style="color: #C7C9E8; font-size: 16px;">
                Compare your resume with job descriptions,
                discover skill gaps and measure your compatibility.
            </p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("### Job Description")
    st.caption("Enter or paste the complete job description below to evaluate how well your resume matches the role.")
    job_description = st.text_area(
        "Paste the Job Description here",
        height=200
    )

    if st.button("Analyze Job Description", use_container_width=True):

        resume_text = st.session_state.get("resume_text", "")

        if not resume_text.strip():
            st.warning("Please upload your resume first!")

        elif not job_description.strip():
            st.warning("Please enter a Job Description.")

        else:

            with st.spinner("Analyzing your profile..."):

                score = calculate_match(
                    resume_text,
                    job_description
                )

                resume_skills = extract_skills(resume_text)
                job_skills = extract_skills(job_description)

                resume_skill_list = [
                    skill
                    for skills in resume_skills.values()
                    for skill in skills
                ]

                required_skills, preferred_skills = extract_priority_skills(
                    job_description
                )

                matched_required = [
                    skill for skill in required_skills
                    if skill in resume_skill_list
                ]

                missing_required = [
                    skill for skill in required_skills
                    if skill not in resume_skill_list
                ]

                matched_preferred = [
                    skill for skill in preferred_skills
                    if skill in resume_skill_list
                ]

                missing_preferred = [
                    skill for skill in preferred_skills
                    if skill not in resume_skill_list
                ]
                job_skill_list = [
                    skill
                    for skills in job_skills.values()
                    for skill in skills
                ]

                matched_skills = [
                    skill for skill in job_skill_list
                    if skill in resume_skill_list
                ]

                missing_skills = [
                    skill for skill in job_skill_list
                    if skill not in resume_skill_list
                ]

            st.success("Analysis completed!")

            st.subheader("Resume Match Score")
            st.markdown("### Your Job Match Results")
            st.metric(
                label="Overall Match Score",
value=f"{score}%"
            )

            st.progress(score/100)
            if score >= 75:
                st.success("Excellent Match! Your profile aligns well with this role.")
            elif score >= 50:
                st.info("Good Match! A few improvements can strengthen your profile.")
            else:
                st.warning("Low Match. Focus on developing the missing skills.")
            st.caption("This score is an estimated measure of resume-job compatibility, not a hiring probability.")
            st.divider()

            st.subheader("Skill Gap Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### Matched Skills")
                st.success(
                    ", ".join(matched_skills)
                    if matched_skills
                    else "No matching skills found."
                )

            with col2:

                st.markdown("### Missing Skills")
                st.warning(
                    ", ".join(missing_skills)
                    if missing_skills
                    else "No missing skills found!"
                )

            if missing_skills:
                st.markdown("### Recommended Next Steps")
                st.info(
        "Consider learning these skills to improve your profile: "
        + ", ".join(missing_skills)
    )
            else:
                st.success("Your resume covers all the identified skills!")
            # Skill Coverage Calculation
            total_weight = (
                2 * len(required_skills) +
                len(preferred_skills)
            )

            earned_weight = (
                2 * len(matched_required) +
                len(matched_preferred)
            )

            if total_weight > 0:
                coverage = (earned_weight / total_weight) * 100
            else:
                coverage = 0

            st.divider()

            st.subheader("Skill Coverage")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Required Skills",
                    len(required_skills)
                )

            with col2:
                st.metric(
                    "Total Matched Skills",
                    len(matched_required)+len(matched_preferred)
                )

            with col3:
                st.metric(
                    "Coverage",
                    f"{coverage:.1f}%"
                )
            with col4:
                st.metric(
                    "Missing Required",
                    len(required_skills) - len(matched_required)
                )

            st.progress(
    min(max(int(coverage), 0), 100),
    text=f"Skill Coverage: {coverage:.1f}%"
)
            st.caption(
                "Coverage is calculated using weighted required "
                "and preferred skills."
            )

            st.divider()

            st.subheader("Personalized Recommendations")
            st.caption(
                "Get personalized learning suggestions based on the skills "
                "missing from your resume."
            )
            recommendations = {

                "Python": "Practice Python programming and problem-solving.",

                "Machine Learning": "Study supervised and unsupervised ML algorithms.",

                "Deep Learning": "Explore neural networks and deep learning fundamentals.",

                "SQL": "Practice SQL queries, joins and database operations.",

                "TensorFlow": "Learn building and training models using TensorFlow.",

                "PyTorch": "Explore neural networks using PyTorch.",

                "Pandas": "Practice data cleaning and manipulation using Pandas.",

                "NumPy": "Improve your understanding of numerical computing.",

                "Scikit-learn": "Practice model training and evaluation using Scikit-learn.",

                "NLP": "Learn text preprocessing and natural language processing."
            }

            if missing_skills:

                for index, skill in enumerate(missing_skills, start=1):

                    suggestion = recommendations.get(
                        skill,
                        f"Explore {skill} and build a practical project."
                    )

                    with st.container(border=True):
                        st.markdown(f"**{index}. {skill}**")
                        st.write(suggestion)

                        if skill in required_skills:
                            st.caption("🔴 High Priority — Required Skill")
                        else:
                            st.caption("🟡 Medium Priority — Preferred Skill")

            else:
                st.success(
                    "Great! All predefined required skills were found in your resume."
                )
            if missing_skills:
                st.markdown("### Suggested Learning Roadmap")

                st.write("**Step 1:** Understand the fundamentals.")
                st.write("**Step 2:** Practice through coding exercises.")
                st.write("**Step 3:** Build a practical project using missing skills.")
                st.write("**Step 4:** Add your newly acquired skills to your resume.")
            st.info("Tip: Focus on required skills first to improve your job compatibility.")
            st.divider()
            st.subheader("Skill Priority Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### Required Skills")

                st.success(
                    "Matched: " + ", ".join(matched_required)
                    if matched_required
                    else "No required skills matched."
                )

                st.error(
                    "Missing: " + ", ".join(missing_required)
                    if missing_required
                    else "No missing required skills!"
                )

            with col2:

                st.markdown("### Preferred Skills")

                st.success(
                    "Matched: " + ", ".join(matched_preferred)
                    if matched_preferred
                    else "No preferred skills matched."
                )

                st.warning(
                    "Missing: " + ", ".join(missing_preferred)
                    if missing_preferred
                    else "All preferred skills found!"
                )
            st.divider()

            st.subheader("Download Your Analysis Report")

            report = generate_report(
                score,
                coverage,
                required_skills,
                matched_required,
                matched_preferred,
                missing_skills
            )

            st.download_button(
                label="📥 Download Analysis Report",
                data=report,
                file_name="SkillSync_Analysis_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )               
# About Page
elif page == "About":

            st.markdown("""
            <div style="
                background: linear-gradient(120deg, #25204B, #252F58);
                padding: 30px;
                border-radius: 16px;
                border: 1px solid #494078;
            ">
                <h1 style="color: white;">About SkillSync</h1>
                <p style="color: #C7C9E8; font-size: 16px;">
                    An intelligent resume analysis and job matching
                    platform designed to help job seekers identify
                    skill gaps and improve career readiness.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### Project Overview")

            st.write(
                "SkillSync analyzes resumes, extracts technical skills, "
                "compares them with job descriptions and calculates an "
                "estimated compatibility score. It helps users identify "
                "missing skills and receive personalized recommendations "
                "for improving their profiles."
            )

            st.divider()

            st.markdown("### Key Features")

            col1, col2 = st.columns(2)

            with col1:
                with st.container(border=True):
                    st.markdown("📄 **Resume Analysis**")
                    st.write(
                        "Extracts technical skills from uploaded PDF resumes."
                    )

                with st.container(border=True):
                    st.markdown("🎯 **Smart Job Matching**")
                    st.write(
                        "Compares resumes with job descriptions using "
                        "text similarity and skill-based scoring."
                    )

            with col2:
                with st.container(border=True):
                    st.markdown("📊 **Skill Gap Analysis**")
                    st.write(
                        "Identifies matched, missing and preferred skills."
                    )

                with st.container(border=True):
                    st.markdown("💡 **Personalized Recommendations**")
                    st.write(
                        "Provides suggestions to improve skills "
                        "and job compatibility."
                    )

            st.divider()

            st.markdown("### Technology Stack")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("**Python**")
                st.caption("Core programming language")

            with col2:
                st.markdown("**Streamlit**")
                st.caption("Interactive web application")

            with col3:
                st.markdown("**Scikit-learn**")
                st.caption("TF-IDF & similarity analysis")

            st.markdown("**Other Libraries:** PyPDF2, Pandas, NumPy, ReportLab")

            st.divider()

            st.markdown("### How It Works")

            st.write("**01 — Upload:** Upload your resume in PDF format.")
            st.write("**02 — Extract:** Extract text and identify technical skills.")
            st.write("**03 — Match:** Compare your resume with a job description.")
            st.write("**04 — Analyze:** View match score and skill coverage.")
            st.write("**05 — Improve:** Get recommendations and download your report.")

            st.divider()

            st.markdown("### Future Scope")

            st.write(
                "- Integration with real-time job listings"
            )
            st.write(
                "- AI-powered resume improvement suggestions"
            )
            st.write(
                "- Learning resource and course recommendations"
            )
            st.write(
                "- Multiple resume and job comparison"
            )
            st.write(
                "- Enhanced ATS compatibility analysis"
            )
