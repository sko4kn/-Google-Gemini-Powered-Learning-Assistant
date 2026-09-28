from gemini_client import generate_text


def answer_question(question: str) -> str:
    prompt = f'''
You are EduGenie, an educational AI assistant.

Answer the student's question clearly and accurately.

Question:
{question}

Instructions:
- Use simple, student-friendly language.
- Explain the concept clearly.
- Include a small example when useful.
- Do not make the answer unnecessarily long.
'''
    return generate_text(prompt, temperature=0.3, max_output_tokens=800)
