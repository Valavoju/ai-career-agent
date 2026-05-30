def calculate_match(resume_skills, required_skills):

    matched = []
    missing = []

    resume_text = " ".join(resume_skills).lower()

    for skill in required_skills:

        words = skill.lower().split()

        if any(word in resume_text for word in words):
            matched.append(skill)
        else:
            missing.append(skill)

    score = int(
        (len(matched) / len(required_skills)) * 100
    ) if required_skills else 0

    return {
        "match_score": score,
        "matching_skills": matched,
        "missing_skills": missing
    }