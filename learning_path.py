from gemini_client import generate_text


def recommend_learning_path(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for a student who wants to learn:

{topic}

Include:

1. Learning Goal
2. Beginner Level
3. Intermediate Level
4. Advanced Level
5. Suggested Timeline
6. Practice Activities
7. Useful Resource Types

Use simple language and make the plan practical for a student.
"""

    return generate_text(
        prompt,
        temperature=0.4,
        max_output_tokens=1500,
    )