from groq_client import client

def generate_advice(role, score, missing_skills):

    prompt = f"""
You are a career advisor.

Role:
{role}

Match Score:
{score}

Missing Skills:
{missing_skills}

Give:
1. Overall evaluation
2. Job readiness
3. Top 3 priorities

Keep under 150 words.
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