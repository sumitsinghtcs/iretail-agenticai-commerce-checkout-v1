import asyncio
from app.llm.grok_provider import GroqProvider

async def test_grok_llm():
    provider = GroqProvider()
    prompt = "Describe London in exactly 10 words."
    response = await provider.generate(prompt)
    print("Response:")
    print(response)

if __name__ == '__main__':
    asyncio.run(test_grok_llm())
