from gemini_client import generate_text


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text.

Requirements:
- Keep the important ideas.
- Use simple language.
- Make it useful for student revision.
- Keep the summary concise.
- Use short paragraphs or bullet points where helpful.

Text:

{text}
"""

    return generate_text(
        prompt,
        temperature=0.3,
        max_output_tokens=1200,
    )