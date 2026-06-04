def calculate_match(resume_skills, required_skills):

    flattened_skills = []

    for category in resume_skills:

        if isinstance(category, dict):

            skills = category.get("skills", [])

            for skill in skills:
                flattened_skills.append(
                    str(skill).lower().strip()
                )

    matched = []
    missing = []

    for skill in required_skills:

        skill_text = str(skill).lower().strip()

        found = False

        for resume_skill in flattened_skills:

            if (
                skill_text == resume_skill
                or skill_text in resume_skill
                or resume_skill in skill_text
            ):
                found = True
                break

        if found:
            matched.append(skill)

        else:
            missing.append(skill)

    score = (
        round(
            (len(matched) / len(required_skills)) * 100
        )
        if required_skills
        else 0
    )

    return {
        "match_score": score,
        "matching_skills": matched,
        "missing_skills": missing
    }