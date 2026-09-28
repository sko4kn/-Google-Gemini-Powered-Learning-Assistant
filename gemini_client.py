import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Please add your Gemini API key to the .env file."
    )

client = genai.Client(api_key=API_KEY)


def generate_text(
    prompt: str,
    temperature: float = 0.3,
    max_output_tokens: int = 800,
) -> str:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        ),
    )

    return response.text or ""