import json
import re

from groq_client import client


def get_role_requirements(role):

    prompt = f"""
You are an expert recruiter.

For the role:

{role}

Generate required skills.

Return ONLY JSON.

{{
    "required_skills": []
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
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
            r'\{.*\}',
            result,
            re.DOTALL
        )

        if match:
            return json.loads(
                match.group()
            )

    except:
        pass

    return {
        "required_skills": []
    }