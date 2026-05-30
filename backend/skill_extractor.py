import json
import re

from groq_client import client

def extract_skills(resume_text):

    prompt = f"""
You are an expert ATS resume analyzer.

Extract ALL technical skills from the resume.

Include:
- Programming Languages
- Frameworks
- Libraries
- Databases
- AI/ML Skills
- Deep Learning
- Tools
- Cloud Skills
- Version Control
- Technologies

Do NOT miss any skill.

Return ONLY valid JSON.

{{
    "skills": [],
    "strengths": [],
    "recommended_role": ""
}}

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content.strip()

    try:
        result = result.replace("```json", "")
        result = result.replace("```", "")

        match = re.search(r'\{.*\}', result, re.DOTALL)

        if match:
            return json.loads(match.group())

    except Exception as e:
        print("JSON Parse Error:", e)

    return {
        "skills": [],
        "strengths": [],
        "recommended_role": ""
    }