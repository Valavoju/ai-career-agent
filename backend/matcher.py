def calculate_match(resume_skills, required_skills):

    flattened_skills = []

    for category in resume_skills:

        if isinstance(category, dict):

            skills = category.get("skills", [])

            for skill in skills:
                flattened_skills.append(skill)

    resume_text = " ".join(flattened_skills).lower()

    matched = []
    missing = []

    for skill in required_skills:

        skill_text = skill.lower()

        if any(
            resume_skill.lower() in skill_text
            or skill_text in resume_skill.lower()
            for resume_skill in flattened_skills
        ):
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