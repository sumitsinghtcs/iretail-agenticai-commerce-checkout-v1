from openai import AsyncOpenAI

from app.llm.base_provider import BaseLLMProvider

from app.utils.config import settings

class GroqProvider(BaseLLMProvider):

    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.GROQ_API_KEY,
            base_url="https://api.groq.com/openai/v1"
        )
        self.model = settings.DEFAULT_MODEL

    async def generate(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.1
        )
        return response.choices[0].message.content
