from groq_client import client


def generate_hr_email(role, recommendation):

    prompt = f"""
Write a professional HR email.

Role:
{role}

Hiring Decision:
{recommendation}

Keep it concise and professional.
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

    return response.choices[0].message.content