import json
import re

from groq_client import client


def generate_roadmap(
    role,
    missing_skills
):

    prompt = f"""
You are an AI Career Mentor.

Create a professional learning roadmap.

Target Role:
{role}

Missing Skills:
{missing_skills}

Return ONLY JSON.

{{
    "readiness": "",
    "estimated_time": "",
    "roadmap": "",
    "expected_outcome": ""
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
        temperature=0.6
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
            data = json.loads(
                match.group()
            )

            return data

    except Exception as e:
        print(
            "Roadmap Agent Error:",
            e
        )

    return {
        "readiness": "Unknown",
        "estimated_time": "",
        "roadmap": "",
        "expected_outcome": ""
    }