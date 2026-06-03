import json
import re

from groq_client import client


def get_hiring_recommendation(
    score,
    matching_skills,
    missing_skills,
    role
):

    prompt = f"""
You are a senior technical recruiter.

Analyze the candidate profile.

Target Role:
{role}

ATS Score:
{score}

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

Return ONLY valid JSON.

{{
    "recommendation": "",
    "confidence_percentage": 0,
    "risk_level": "",
    "assessment": "",
    "action": ""
}}
Rules:

- confidence_percentage must be an integer between 0 and 100.
- recommendation must be one of:
  Strong Hire
  Hire
  Borderline
  Not Recommended
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    result = response.choices[0].message.content.strip()

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
            r'\{.*\}',
            result,
            re.DOTALL
        )

        if match:
            return json.loads(
                match.group()
            )

    except Exception as e:
        print(
            "Hiring Agent Error:",
            e
        )

    return {
        "recommendation":
            "Borderline",

         "confidence_percentage": 70,

        "risk_level":
            "Medium",

        "assessment":
            "Unable to generate assessment.",

        "action":
            "Manual review recommended."
    }