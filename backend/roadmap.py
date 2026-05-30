from groq_client import client

def generate_roadmap(role, missing_skills):

    prompt = f"""
Create a concise learning roadmap.

Target Role:
{role}

Missing Skills:
{missing_skills}

Keep under 200 words.
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

    return response.choices[0].message.content