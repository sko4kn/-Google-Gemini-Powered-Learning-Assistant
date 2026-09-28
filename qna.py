from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Explain in simple language.
- Give enough detail for a student to understand.
- Use examples when helpful.
- Do not unnecessarily make the answer very long.
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=800,
    )