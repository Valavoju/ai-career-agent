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
3. rounds MUST contain at least 4 interview rounds.
4. Every round MUST contain:
   - round_name
   - duration
   - description
   - questions

5. focus_areas MUST contain ONLY 4-6 HIGH LEVEL topics.

GOOD:
[
 "Machine Learning",
 "Deep Learning",
 "Computer Vision",
 "Cloud Computing",
 "AI Engineering"
]

BAD:
[
 "TensorFlow",
 "Keras",
 "PyTorch",
 "NumPy",
 "Pandas",
 "Matplotlib",
 "Seaborn"
]

Return JSON exactly like:

{{
  "difficulty": "Medium",
  "duration": "60-90 minutes",

  "rounds": [
    {{
      "round_name": "Introduction and Icebreaker",
      "duration": "10 minutes",
      "description": "Brief introduction of the candidate.",
      "questions": [
        "Tell us about yourself."
      ]
    }},
    {{
      "round_name": "Technical Skills Assessment",
      "duration": "30 minutes",
      "description": "Evaluate technical knowledge.",
      "questions": [
        "Explain machine learning."
      ]
    }}
  ],

  "focus_areas": [
    "Machine Learning",
    "Deep Learning",
    "Computer Vision",
    "AI Engineering"
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
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if match:

            data = json.loads(match.group())

            # Limit focus areas
            if len(data.get("focus_areas", [])) > 6:
                data["focus_areas"] = data["focus_areas"][:6]

            # Normalize rounds
            cleaned_rounds = []

            for round_item in data.get("rounds", []):

                cleaned_rounds.append({

                    "round_name":
                        round_item.get(
                            "round_name",
                            round_item.get(
                                "round",
                                round_item.get(
                                    "name",
                                    "Interview Round"
                                )
                            )
                        ),

                    "duration":
                        round_item.get(
                            "duration",
                            round_item.get(
                                "estimated_time",
                                round_item.get(
                                    "time",
                                    "15 minutes"
                                )
                            )
                        ),

                    "description":
                        round_item.get(
                            "description",
                            ""
                        ),

                    "questions":
                        round_item.get(
                            "questions",
                            []
                        )

                })

            data["rounds"] = cleaned_rounds

            # Fallback rounds
            if not data["rounds"]:

                data["rounds"] = [

                    {
                        "round_name":
                        "Introduction and Icebreaker",

                        "duration":
                        "10 minutes",

                        "description":
                        "Brief introduction of the candidate followed by an icebreaker question.",

                        "questions": [
                            "Tell us about yourself."
                        ]
                    },

                    {
                        "round_name":
                        "Technical Skills Assessment",

                        "duration":
                        "30 minutes",

                        "description":
                        "Evaluate technical knowledge related to the target role.",

                        "questions": [
                            "Explain a project you worked on."
                        ]
                    },

                    {
                        "round_name":
                        "Behavioral Questions",

                        "duration":
                        "20 minutes",

                        "description":
                        "Assess communication, teamwork and adaptability.",

                        "questions": [
                            "Describe a challenging situation."
                        ]
                    },

                    {
                        "round_name":
                        "Project Discussion",

                        "duration":
                        "20 minutes",

                        "description":
                        "Discuss practical implementation and project experience.",

                        "questions": [
                            "Walk us through your project."
                        ]
                    }

                ]

            # Fallback focus areas
            if not data.get("focus_areas"):

                data["focus_areas"] = [
                    "AI Engineering",
                    "Machine Learning",
                    "Deep Learning",
                    "Computer Vision"
                ]

            # Fallback strategy
            if not data.get("strategy"):

                data["strategy"] = (
                    "Evaluate the candidate on technical knowledge, "
                    "problem-solving ability, practical implementation "
                    "experience, communication skills and project exposure."
                )

            return data

    except Exception as e:

        print(
            "Interview Agent Error:",
            e
        )

    return {

        "difficulty": "Medium",

        "duration": "60-90 minutes",

        "rounds": [

            {
                "round_name":
                "Introduction and Icebreaker",

                "duration":
                "10 minutes",

                "description":
                "Brief introduction of the candidate followed by an icebreaker question.",

                "questions": [
                    "Tell us about yourself."
                ]
            },

            {
                "round_name":
                "Technical Skills Assessment",

                "duration":
                "30 minutes",

                "description":
                "Evaluate technical knowledge related to the target role.",

                "questions": [
                    "Explain a project you worked on."
                ]
            },

            {
                "round_name":
                "Behavioral Questions",

                "duration":
                "20 minutes",

                "description":
                "Assess communication, teamwork and adaptability.",

                "questions": [
                    "Describe a challenging situation."
                ]
            },

            {
                "round_name":
                "Project Discussion",

                "duration":
                "20 minutes",

                "description":
                "Discuss practical implementation and project experience.",

                "questions": [
                    "Walk us through your project."
                ]
            }

        ],

        "focus_areas": [
            "AI Engineering",
            "Machine Learning",
            "Deep Learning",
            "Computer Vision"
        ],

        "strategy":
        "Evaluate the candidate on technical knowledge, problem-solving ability, practical implementation experience, communication skills and project exposure."

    }