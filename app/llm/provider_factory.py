from app.utils.config import settings

from app.llm.grok_provider import GroqProvider
from app.llm.openrouter_provider import OpenRouterProvider


class ProviderFactory:

    @staticmethod
    def get_provider():

        provider = (
            settings.LLM_PROVIDER
            .lower()
            .strip()
        )

        if provider == "groq":
            return GroqProvider()

        if provider == "openrouter":
            return OpenRouterProvider()

        raise ValueError(
            f"Unsupported provider: {provider}"
        )