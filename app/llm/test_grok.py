from openai import OpenAI
from app.utils.config import settings

client = OpenAI(
    api_key=settings.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Describe London in exactly 100 words."
        }
    ],
    temperature=0
)

print("\nResponse:")
print(response.choices[0].message.content)