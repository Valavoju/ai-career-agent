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

Create a detailed interview plan.

Role:
{role}

Recommendation:
{recommendation}

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

IMPORTANT:

1. Return ONLY valid JSON.
2. Do NOT return markdown.
3. rounds MUST contain at least 3 interview rounds.
4. focus_areas MUST contain at least 4 items.

Return JSON exactly like:

{{
  "difficulty": "Medium",
  "duration": "60 Minutes",

  "rounds": [
    {{
      "round_name": "Introduction and Background",
      "duration": "15 minutes"
    }},
    {{
      "round_name": "Technical Skills Assessment",
      "duration": "30 minutes"
    }},
    {{
      "round_name": "System Design and Problem Solving",
      "duration": "15 minutes"
    }}
  ],

  "focus_areas": [
    "AI Engineering",
    "Machine Learning",
    "Deep Learning",
    "Cloud Computing"
  ],

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

        result = result.replace("```json", "")
        result = result.replace("```", "")

        match = re.search(
            r'\{.*\}',
            result,
            re.DOTALL
        )

        if match:

            data = json.loads(match.group())

            if not data.get("rounds"):
                data["rounds"] = [
                    {
                        "round_name":
                        "Introduction and Background",
                        "duration":
                        "15 minutes"
                    },
                    {
                        "round_name":
                        "Technical Skills Assessment",
                        "duration":
                        "30 minutes"
                    },
                    {
                        "round_name":
                        "System Design and Problem Solving",
                        "duration":
                        "15 minutes"
                    }
                ]

            if not data.get("focus_areas"):
                data["focus_areas"] = [
                    "AI Engineering",
                    "Machine Learning",
                    "Deep Learning",
                    "Cloud Computing"
                ]

            return data

    except Exception as e:

        print(
            "Interview Agent Error:",
            e
        )

    return {
        "difficulty": "Medium",
        "duration": "60 Minutes",

        "rounds": [
            {
                "round_name":
                "Introduction and Background",
                "duration":
                "15 minutes"
            },
            {
                "round_name":
                "Technical Skills Assessment",
                "duration":
                "30 minutes"
            },
            {
                "round_name":
                "System Design and Problem Solving",
                "duration":
                "15 minutes"
            }
        ],

        "focus_areas": [
            "AI Engineering",
            "Machine Learning",
            "Deep Learning",
            "Cloud Computing"
        ],

        "strategy":
        "Candidate will be assessed on technical knowledge, problem solving and practical implementation skills."
    }