import json
import re

from groq_client import client


def generate_roadmap(role, missing_skills):

    prompt = f"""
Create a learning roadmap for:

Role:
{role}

Missing Skills:
{missing_skills}

IMPORTANT RULES:

1. Return ONLY valid JSON.
2. Do NOT return markdown.
3. Do NOT use fields:
   - topic
   - subtopics
   - learning_resources
   - learning_materials
   - projects

4. Every roadmap item MUST contain ONLY:

[
  {{
    "skill": "",
    "description": "",
    "estimated_time": "",
    "resources": []
  }}
]

5. Every phase value MUST be an ARRAY.

CORRECT:

{{
  "Phase 1": [
    {{
      "skill": "Python",
      "description": "Learn Python basics",
      "estimated_time": "2 weeks",
      "resources": [
        "Python.org",
        "Codecademy"
      ]
    }}
  ]
}}

WRONG:

{{
  "Phase 1": {{
    "topic": "Python"
  }}
}}

Return ONLY JSON:

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

        result = result.replace("```json", "")
        result = result.replace("```", "")

        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if match:

            data = json.loads(match.group())

            # Normalize roadmap structure
            for phase_name, phase_data in data.get("roadmap", {}).items():

                if not isinstance(phase_data, list):
                    data["roadmap"][phase_name] = []
                    continue

                cleaned = []

                for item in phase_data:

                    cleaned.append({
                        "skill": item.get(
                            "skill",
                            item.get("topic", "")
                        ),

                        "description": item.get(
                            "description",
                            item.get(
                                "expected_outcome",
                                ""
                            )
                        ),

                        "estimated_time": item.get(
                            "estimated_time",
                            item.get(
                                "Time",
                                ""
                            )
                        ),

                        "resources": item.get(
                            "resources",
                            item.get(
                                "learning_resources",
                                []
                            )
                        )
                    })

                data["roadmap"][phase_name] = cleaned

            return data

    except Exception as e:

        print(
            "Roadmap Agent Error:",
            e
        )

    return {
        "readiness": "Unknown",
        "estimated_time": "",
        "roadmap": {},
        "expected_outcome": ""
    }