from groq_client import client
import json
import re

def get_role_requirements(role):

    prompt = f"""
For the role: {role}

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
        match = re.search(r'\{.*\}', result, re.DOTALL)

        if match:
            return json.loads(match.group())

    except Exception:
        pass

    return {
        "required_skills": []
    }