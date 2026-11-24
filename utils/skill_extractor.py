
import re

SKILLS = {
    "Programming Languages": [
        "Python", "Java", "C", "C++", "JavaScript"
    ],

    "AI & Machine Learning": [
        "Machine Learning", "Deep Learning",
        "Artificial Intelligence", "NLP",
        "TensorFlow", "PyTorch", "Scikit-learn"
    ],

    "Data Science": [
        "Pandas", "NumPy", "Matplotlib",
        "Data Analysis", "Data Visualization"
    ],

    "Database & Tools": [
        "SQL", "MySQL", "MongoDB",
        "Git", "GitHub", "Power BI", "Excel"
    ],

    "Web Development": [
        "HTML", "CSS", "React", "Flask",
        "Django", "Streamlit"
    ]
}


def extract_skills(text):

    detected_skills = {}

    for category, skills in SKILLS.items():

        matched = []

        for skill in skills:

            pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

            if re.search(pattern, text, re.IGNORECASE):
                matched.append(skill)

        if matched:
            detected_skills[category] = matched

    return detected_skills

def extract_priority_skills(text):

    required_text = ""
    preferred_text = ""

    current_section = None

    for line in text.splitlines():

        heading = line.strip().strip("*# :").lower()

        if heading in [
            "required skills",
            "requirements",
            "must-have skills"
        ]:
            current_section = "required"
            continue

        elif heading in [
            "preferred skills",
            "nice to have",
            "good to have"
        ]:
            current_section = "preferred"
            continue

        elif heading in [
            "responsibilities",
            "about the role",
            "eligibility",
            "experience",
            "job title"
        ]:
            current_section = None

        if current_section == "required":
            required_text += line + " "

        elif current_section == "preferred":
            preferred_text += line + " "

    required = extract_skills(required_text)
    preferred = extract_skills(preferred_text)

    required_list = [
        skill
        for skills in required.values()
        for skill in skills
    ]

    preferred_list = [
        skill
        for skills in preferred.values()
        for skill in skills
        if skill not in required_list
    ]

    # Fallback if no priority sections are found
    if not required_list and not preferred_list:
        all_skills = extract_skills(text)

        required_list = [
            skill
            for skills in all_skills.values()
            for skill in skills
        ]

    return required_list, preferred_list
