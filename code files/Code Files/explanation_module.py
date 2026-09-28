from gemini_client import generate_text


def explain_concept(concept: str) -> str:
    prompt = f'''
You are EduGenie, an educational AI assistant.

Explain the following concept to a student in simple language:

Concept:
{concept}

Instructions:
- Start with a simple definition.
- Explain the main idea using short sections or bullets.
- Give a simple real-world or educational example.
- Keep the explanation easy to understand.
'''
    return generate_text(prompt, temperature=0.3, max_output_tokens=800)
