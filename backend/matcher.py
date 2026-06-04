from difflib import SequenceMatcher


def normalize_skill(skill):

    skill = str(skill).lower().strip()

    synonyms = {

        "ml": "machine learning",
        "dl": "deep learning",
        "nlp": "natural language processing",
        "cv": "computer vision",

        "amazon web services": "aws",
        "google cloud platform": "google cloud",
        "gcp": "google cloud",

        "tensor flow": "tensorflow",
        "py torch": "pytorch",

        "scikit learn": "scikit-learn",
        "sklearn": "scikit-learn",

        "git version control": "git",
        "github": "git",

        "mysql database": "sql",
        "postgresql": "sql",
        "sqlite": "sql",
    }

    return synonyms.get(skill, skill)


def fuzzy_match(skill1, skill2):

    ratio = SequenceMatcher(
        None,
        skill1,
        skill2
    ).ratio()

    return ratio >= 0.80


def calculate_match(
    resume_skills,
    required_skills
):

    flattened_skills = []

    for category in resume_skills:

        if isinstance(category, dict):

            skills = category.get(
                "skills",
                []
            )

            for skill in skills:

                flattened_skills.append(
                    normalize_skill(skill)
                )

        else:

            flattened_skills.append(
                normalize_skill(category)
            )

    matched = []
    missing = []

    for skill in required_skills:

        skill_text = normalize_skill(skill)

        found = False

        for resume_skill in flattened_skills:

            # Exact match

            if skill_text == resume_skill:

                found = True
                break

            # Partial match

            if (
                skill_text in resume_skill
                or resume_skill in skill_text
            ):

                found = True
                break

            # Fuzzy match

            if fuzzy_match(
                skill_text,
                resume_skill
            ):

                found = True
                break

        if found:

            matched.append(skill)

        else:

            missing.append(skill)

    score = (
        round(
            (
                len(matched)
                / len(required_skills)
            ) * 100
        )
        if required_skills
        else 0
    )

    return {

        "match_score": score,

        "matching_skills": matched,

        "missing_skills": missing
    }