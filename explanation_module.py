from gemini_client import generate_text


def explain_concept(concept: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Explain the following concept to a student in simple and easy-to-understand language.

Concept:
{concept}

Instructions:
- Explain the concept clearly.
- Use simple language.
- Give an example when helpful.
- Organize the explanation with short sections or bullet points.
- Avoid unnecessary complexity.
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=800,
    )