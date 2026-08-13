from langchain_groq import ChatGroq
from llm.base import BaseLLM


class GroqLLM(BaseLLM):

    def __init__(
        self,
        api_key: str,
        model_name: str = "llama-3.3-70b-versatile"
    ):

        self.llm = ChatGroq(
            api_key=api_key,
            model=model_name
        )

    def generate(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        return response.content