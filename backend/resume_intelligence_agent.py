import json
import re

from groq_client import client


def generate_candidate_intelligence(
    resume_text,
    role
):

    prompt = f"""
You are a senior AI recruiter.

Analyze the candidate resume.

Target Role:
{role}

Resume:
{resume_text}

Return ONLY JSON.

{{
    "profile_summary": "",
    "strengths": [],
    "weaknesses": [],
    "career_path": ""
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
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if match:
            return json.loads(
                match.group()
            )

    except Exception as e:

        print(
            "Resume Intelligence Error:",
            e
        )

    return {
        "profile_summary":
            "Profile analysis unavailable.",

        "strengths": [],

        "weaknesses": [],

        "career_path":
            role
    }