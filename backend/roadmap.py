import json
import re

from groq_client import client


def generate_roadmap(role, missing_skills):

    prompt = f"""
You are an expert AI Career Mentor.

Create a COMPLETE learning roadmap.

Role:
{role}

Missing Skills:
{missing_skills}

IMPORTANT:

1. Return ONLY valid JSON.
2. Do NOT return markdown.
3. roadmap MUST be an OBJECT.
4. Every phase MUST contain an ARRAY.
5. Every roadmap item MUST contain:

{{
  "skill": "",
  "description": "",
  "estimated_time": "",
  "resources": []
}}

Example:

{{
  "readiness": "Beginner",

  "estimated_time": "6-12 months",

  "roadmap": {{

    "Phase 1: Foundations (1-2 months)": [

      {{
        "skill": "Python Programming",

        "description":
        "Learn Python syntax, OOP, functions and problem solving.",

        "estimated_time":
        "2 weeks",

        "resources": [
          "Python.org",
          "Codecademy Python Course"
        ]
      }}

    ],

    "Phase 2: Machine Learning (2-3 months)": [

      {{
        "skill": "Scikit-Learn",

        "description":
        "Learn ML algorithms and model training.",

        "estimated_time":
        "3 weeks",

        "resources": [
          "Scikit-Learn Documentation",
          "Coursera Machine Learning"
        ]
      }}

    ]

  }},

  "expected_outcome":
  "Become job-ready for the selected role."
}}

Return ONLY JSON.
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

    print("\n==============================")
    print("RAW ROADMAP RESPONSE")
    print("==============================")
    print(result)
    print("==============================\n")

    try:

        result = result.replace("```json", "")
        result = result.replace("```", "")

        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if not match:
            raise Exception("No JSON found")

        data = json.loads(match.group())

        # --------------------------------------------------
        # Safety checks for roadmap
        # --------------------------------------------------

        roadmap_data = data.get("roadmap")

        if roadmap_data is None:
            roadmap_data = {}

        if isinstance(roadmap_data, str):
            roadmap_data = {}

        if isinstance(roadmap_data, list):

            fixed_roadmap = {}

            for phase in roadmap_data:

                phase_name = phase.get(
                    "phase",
                    "Learning Phase"
                )

                skills_data = []

                for skill in phase.get(
                    "skills",
                    []
                ):

                    skills_data.append({

                        "skill":
                        skill,

                        "description":
                        f"Learn {skill} thoroughly with practical projects and hands-on exercises.",

                        "estimated_time":
                        "1-2 weeks",

                        "resources":
                        []

                    })

                fixed_roadmap[
                    phase_name
                ] = skills_data

            roadmap_data = fixed_roadmap

        if not isinstance(
            roadmap_data,
            dict
        ):
            roadmap_data = {}

        data["roadmap"] = roadmap_data

        # --------------------------------------------------
        # Normalize roadmap structure
        # --------------------------------------------------

        for phase_name, phase_data in roadmap_data.items():

            if not isinstance(
                phase_data,
                list
            ):
                roadmap_data[
                    phase_name
                ] = []
                continue

            cleaned = []

            for item in phase_data:

                if not isinstance(
                    item,
                    dict
                ):
                    continue

                cleaned.append({

                    "skill":
                    item.get(
                        "skill",
                        item.get(
                            "Skill",
                            ""
                        )
                    ),

                    "description":
                    item.get(
                        "description",
                        item.get(
                            "Description",
                            ""
                        )
                    ),

                    "estimated_time":
                    item.get(
                        "estimated_time",
                        item.get(
                            "Estimated Time",
                            ""
                        )
                    ),

                    "resources":
                    item.get(
                        "resources",
                        item.get(
                            "Resources",
                            []
                        )
                    )

                })

            roadmap_data[
                phase_name
            ] = cleaned

        data["roadmap"] = roadmap_data

        if not data.get("readiness"):
            data["readiness"] = "Beginner"

        if not data.get("estimated_time"):
            data["estimated_time"] = "6-12 months"

        if not data.get("expected_outcome"):
            data["expected_outcome"] = (
                "Become job-ready for the selected role."
            )

        return data

    except Exception as e:

        print(
            "Roadmap Agent Error:",
            e
        )

    return {

        "readiness":
        "Beginner",

        "estimated_time":
        "6-12 months",

        "roadmap": {

            "Phase 1: Foundations": [

                {
                    "skill":
                    "Python Programming",

                    "description":
                    "Learn Python fundamentals and problem solving.",

                    "estimated_time":
                    "2 weeks",

                    "resources": [
                        "Python.org",
                        "Codecademy Python Course"
                    ]
                }

            ]

        },

        "expected_outcome":
        "Become job-ready for the selected role."

    }