from openai import AsyncOpenAI

from app.llm.base_provider import BaseLLMProvider

from app.utils.config import settings


class OpenRouterProvider(
    BaseLLMProvider
):

    def __init__(self):

        self.client = AsyncOpenAI(
            api_key=settings.OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

        self.model = ("meta-llama/llama-3.3-70b-instruct")
        #self.model = ("Fusion")
        #self.model = ("Owl Alpha")
        #self.model = ("Pareto Code Router")
        #self.model = ("MiniMax-M3")
        #self.model = ("MiniMax-M3.5")
        
    async def generate(
            self,
            prompt: str
    ) -> str:

        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        return (
            response
            .choices[0]
            .message
            .content
        )