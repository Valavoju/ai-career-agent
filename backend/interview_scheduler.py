import json
import re

from groq_client import client


def generate_interview_plan(
    role,
    recommendation,
    matching_skills,
    missing_skills
):

    prompt = f"""
You are a senior technical interviewer.

Create a personalized interview strategy.

Role:
{role}

Recommendation:
{recommendation}

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

Return ONLY JSON.

{{
    "difficulty": "",
    "duration": "",
    "rounds": [],
    "focus_areas": [],
    "strategy": ""
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5
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
            "Interview Agent Error:",
            e
        )

    return {
        "difficulty": "Medium",
        "duration": "45 Minutes",
        "rounds": [],
        "focus_areas": [],
        "strategy": ""
    }