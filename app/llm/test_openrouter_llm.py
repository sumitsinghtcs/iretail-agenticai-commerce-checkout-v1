import asyncio
from app.llm.openrouter_provider import OpenRouterProvider

async def test_openrouter_llm():
    provider = OpenRouterProvider()
    prompt = "Describe Paris in exactly 10 words."
    response = await provider.generate(prompt)
    print("Response:")
    print(response)

if __name__ == '__main__':
    asyncio.run(test_openrouter_llm())
