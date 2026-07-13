from typing import Dict, List, Optional

from .providers import get_llm_provider
from config import LLM_PROVIDER, LLM_MODEL_NAME, LLM_NUM_CTX, LLM_NUM_PREDICT, LLM_TEMPERATURE


class LLMManager:
    def __init__(self, model_name: Optional[str] = None):
        self.model_name = model_name or LLM_MODEL_NAME
        self.provider = get_llm_provider(LLM_PROVIDER, self.model_name)
        self.options = {
            "num_ctx": LLM_NUM_CTX,
            "num_predict": LLM_NUM_PREDICT,
            "temperature": LLM_TEMPERATURE,
        }

    def generate(self, prompt: str, system: Optional[str] = None) -> str:
        return self.provider.generate(prompt=prompt, system=system, options=self.options)

    def generate_with_options(self, prompt: str, system: Optional[str] = None, options: Optional[Dict] = None) -> str:
        merged_options = {**self.options, **(options or {})}
        return self.provider.generate(prompt=prompt, system=system, options=merged_options)
