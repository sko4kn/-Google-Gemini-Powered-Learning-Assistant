import json
from gemini_client import generate_text


def generate_quiz(topic: str):
    prompt = f'''
Create a quiz for the following educational topic:

Topic:
{topic}

Return ONLY valid JSON in this exact structure:
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

Rules:
- Generate exactly 3 questions.
- Each question must have exactly 4 options: A, B, C, D.
- correct_answer must be only A, B, C, or D.
- Include a short explanation for each answer.
- Return JSON only. Do not use Markdown code fences.
'''

    raw = generate_text(prompt, temperature=0.3, max_output_tokens=1200).strip()

    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError("The AI returned invalid quiz JSON.") from exc

    questions = data.get("questions")
    if not isinstance(questions, list) or len(questions) != 3:
        raise ValueError("Quiz must contain exactly 3 questions.")

    for question in questions:
        options = question.get("options", {})
        if set(options.keys()) != {"A", "B", "C", "D"}:
            raise ValueError("Each quiz question must contain A-D options.")
        if question.get("correct_answer") not in {"A", "B", "C", "D"}:
            raise ValueError("Invalid correct answer in quiz.")

    return data
