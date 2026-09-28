import json
import re

from gemini_client import generate_text


def _clean_json(text: str) -> str:
    text = text.strip()

    # Remove markdown code fences if Gemini returns them.
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)

    return text.strip()


def generate_quiz(topic: str):
    prompt = f"""
Create a short educational quiz about the following topic:

{topic}

Return EXACTLY 3 multiple-choice questions.

Each question must have:
- question
- options: exactly 4 options
- correct_answer: one of A, B, C, or D
- explanation

Return ONLY valid JSON.

Use this exact structure:

{{
  "questions": [
    {{
      "question": "Question text",
      "options": {{
        "A": "Option A",
        "B": "Option B",
        "C": "Option C",
        "D": "Option D"
      }},
      "correct_answer": "A",
      "explanation": "Short explanation"
    }}
  ]
}}
"""

    response = generate_text(
        prompt,
        temperature=0.4,
        max_output_tokens=1800,
    )

    cleaned = _clean_json(response)

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "error": "Gemini returned invalid quiz data.",
            "raw": response,
        }

    questions = data.get("questions")

    if not isinstance(questions, list):
        return {
            "error": "Quiz response does not contain a questions list."
        }

    if len(questions) != 3:
        return {
            "error": "Quiz must contain exactly 3 questions."
        }

    for question in questions:
        if not isinstance(question, dict):
            return {
                "error": "Invalid question format."
            }

        if "question" not in question:
            return {
                "error": "A quiz question is missing its question text."
            }

        options = question.get("options")

        if not isinstance(options, dict):
            return {
                "error": "A quiz question is missing its options."
            }

        required_options = ["A", "B", "C", "D"]

        if any(option not in options for option in required_options):
            return {
                "error": "Every question must have exactly four options: A, B, C and D."
            }

        if question.get("correct_answer") not in required_options:
            return {
                "error": "Correct answer must be A, B, C or D."
            }

    return data