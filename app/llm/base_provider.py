from abc import ABC
from abc import abstractmethod


class BaseLLMProvider(ABC):

    @abstractmethod
    async def generate(
            self,
            prompt: str
    ) -> str:
        pass