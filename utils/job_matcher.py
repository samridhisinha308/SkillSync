
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.skill_extractor import extract_priority_skills


def calculate_match(resume_text, job_description):

    # Calculate text similarity
    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    text_score = similarity[0][0] * 100

    # Extract required and preferred skills
    resume_skills, _ = extract_priority_skills(resume_text)

    required_skills, preferred_skills = extract_priority_skills(
        job_description
    )

    # Identify matched skills
    matched_required = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    matched_preferred = [
        skill for skill in preferred_skills
        if skill in resume_skills
    ]

    # Calculate weighted skill coverage
    total_weight = (
        2 * len(required_skills) +
        len(preferred_skills)
    )

    earned_weight = (
        2 * len(matched_required) +
        len(matched_preferred)
    )

    if total_weight > 0:
        skill_score = (
            earned_weight / total_weight
        ) * 100
    else:
        skill_score = 0

    # Calculate final score
    final_score = (
        0.6 * text_score +
        0.4 * skill_score
    )

    return round(final_score, 2)
