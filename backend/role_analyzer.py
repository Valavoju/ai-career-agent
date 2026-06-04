import json
import re

from groq_client import client


def get_role_requirements(role):

    prompt = f"""
You are an expert recruiter.

For the role:

{role}

Return ONLY a flat list of required skills.

Rules:
1. Return ONLY JSON.
2. Do NOT return explanations.
3. Do NOT return categories.
4. Do NOT return nested objects.
5. Do NOT return subskills.

Example:

{{
    "required_skills": [
        "Python",
        "Java",
        "Machine Learning",
        "TensorFlow",
        "Git",
        "Docker"
    ]
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    try:

        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if match:

            data = json.loads(
                match.group()
            )

            flattened_skills = []

            for item in data.get(
                "required_skills",
                []
            ):

                # Normal skill string

                if isinstance(
                    item,
                    str
                ):
                    flattened_skills.append(
                        item
                    )

                # AI returned object

                elif isinstance(
                    item,
                    dict
                ):

                    if "name" in item:
                        flattened_skills.append(
                            item["name"]
                        )

                    if "subskills" in item:

                        for subskill in item[
                            "subskills"
                        ]:

                            flattened_skills.append(
                                subskill
                            )

            flattened_skills = list(
                dict.fromkeys(
                    flattened_skills
                )
            )

            print(
                "REQUIRED SKILLS =",
                flattened_skills
            )

            return {
                "required_skills":
                flattened_skills
            }

    except Exception as e:

        print(
            "ROLE ANALYZER ERROR:",
            e
        )

    return {
        "required_skills": []
    }