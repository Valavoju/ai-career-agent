import json
import re

from groq_client import client


def get_hiring_recommendation(
    score,
    matching_skills,
    missing_skills,
    role,
    resume_text
):

    # ------------------------
    # Rule-Based Decision
    # ------------------------

    if score >= 85:

        recommendation = "Strong Hire"
        confidence = 95
        risk = "Low"

    elif score >= 70:

        recommendation = "Hire"
        confidence = 85
        risk = "Low"

    elif score >= 50:

        recommendation = "Borderline"
        confidence = 70
        risk = "Medium"

    else:

        recommendation = "Not Recommended"
        confidence = 50
        risk = "High"

    # ------------------------
    # AI Assessment Generator
    # ------------------------

    prompt = f"""
You are a senior technical recruiter.

Generate a short assessment.

Role:
{role}

ATS Score:
{score}

Matching Skills:
{matching_skills}

Missing Skills:
{missing_skills}

Recommendation:
{recommendation}

Return ONLY JSON.

{{
    "assessment": "",
    "action": ""
}}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content.strip()

        result = result.replace("```json", "")
        result = result.replace("```", "")

        match = re.search(
            r"\{.*\}",
            result,
            re.DOTALL
        )

        if match:

            ai_response = json.loads(
                match.group()
            )

            return {

                "recommendation":
                    recommendation,

                "confidence_percentage":
                    confidence,

                "risk_level":
                    risk,

                "assessment":
                    ai_response.get(
                        "assessment",
                        ""
                    ),

                "action":
                    ai_response.get(
                        "action",
                        ""
                    )
            }

    except Exception as e:

        print(
            "Hiring Agent Error:",
            e
        )

    return {

        "recommendation":
            recommendation,

        "confidence_percentage":
            confidence,

        "risk_level":
            risk,

        "assessment":
            f"Candidate matched {len(matching_skills)} skills and missed {len(missing_skills)} skills.",

        "action":
            "Further review recommended."
    }