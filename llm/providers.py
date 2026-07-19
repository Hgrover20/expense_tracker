from abc import ABC, abstractmethod
from typing import Dict, Optional

from config import LLM_HOST


class BaseLLMProvider(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    @abstractmethod
    def generate(self, prompt: str, system: Optional[str] = None, options: Optional[Dict] = None) -> str:
        pass


class OllamaProvider(BaseLLMProvider):
    def __init__(self, model_name: str, host: str):
        super().__init__(model_name)
        try:
            import ollama
        except ImportError as exc:
            raise ImportError("ollama package is required for OllamaProvider") from exc

        self.client = ollama.Client(host=host)

    def generate(self, prompt: str, system: Optional[str] = None, options: Optional[Dict] = None) -> str:
        response = self.client.generate(
            model=self.model_name,
            prompt=prompt,
            system=system,
            stream=False,
            options=options or {},
        )
        return response["response"]


def get_llm_provider(provider_name: str, model_name: str) -> BaseLLMProvider:
    provider_name = provider_name.lower()
    if provider_name == "ollama":
        return OllamaProvider(model_name=model_name, host=LLM_HOST)

    raise ValueError(
        f"Unsupported LLM provider '{provider_name}'. Supported providers: ollama"
    )
