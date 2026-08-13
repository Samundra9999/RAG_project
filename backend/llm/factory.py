from llm.groq import GroqLLM
from llm.gemini import GeminiLLM


def get_llm(
    llm_type: str,
    api_key: str,
    model_name: str = None
):

    if llm_type == "groq":
        return GroqLLM(
            api_key=api_key,
            model_name=model_name or "llama-3.3-70b-versatile"
        )

    if llm_type == "gemini":
        return GeminiLLM(
            api_key=api_key,
            model_name=model_name or "gemini-2.5-flash"
        )

    raise ValueError(f"Unknown llm type: {llm_type}")