from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
)


def ask_llm(query: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Ты поиск фильмов. Отвечай кратко списком."},
            {"role": "user", "content": query},
        ],
    )
    return response.choices[0].message.content.lower()
