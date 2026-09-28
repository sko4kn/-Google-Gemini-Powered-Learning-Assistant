from gemini_client import generate_text


def recommend_learning_path(topic: str) -> str:
    prompt = f'''
Create a learning path for the following topic:

Topic:
{topic}

Include:
1. Learning goal
2. Beginner level
3. Intermediate level
4. Advanced level
5. Suggested timeline
6. Practice activities
7. Useful resource types

Keep the plan practical, clear, and student-friendly.
'''
    return generate_text(prompt, temperature=0.3, max_output_tokens=1000)
