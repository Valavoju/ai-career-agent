def calculate_match(resume_skills, required_skills):

    flattened_skills = []

    for category in resume_skills:

        if isinstance(category, dict):

            skills = category.get("skills", [])

            for skill in skills:
                flattened_skills.append(str(skill))

    matched = []
    missing = []

    for skill in required_skills:

        # Handle dict skills coming from AI
        if isinstance(skill, dict):

            if "skill" in skill:
                skill_text = str(skill["skill"]).lower()

            else:
                skill_text = str(skill).lower()

        else:
            skill_text = str(skill).lower()

        found = False

        for resume_skill in flattened_skills:

            resume_skill_text = str(resume_skill).lower()

            if (
                resume_skill_text in skill_text
                or skill_text in resume_skill_text
            ):
                found = True
                break

        if found:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (
        int((len(matched) / len(required_skills)) * 100)
        if required_skills
        else 0
    )

    return {
        "match_score": score,
        "matching_skills": matched,
        "missing_skills": missing
    }