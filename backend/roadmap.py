import json
import re

from groq_client import client


def generate_roadmap(
    role,
    missing_skills
):

    prompt = f"""
Create a roadmap for:

Role:
{role}

Missing Skills:
{missing_skills}

Return ONLY JSON in this exact format:

{{
  "readiness": "",
  "estimated_time": "",

  "roadmap": {{

    "Phase 1": [
      {{
        "skill": "",
        "description": "",
        "estimated_time": "",
        "resources": []
      }}
    ],

    "Phase 2": [
      {{
        "skill": "",
        "description": "",
        "estimated_time": "",
        "resources": []
      }}
    ]
  }},

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