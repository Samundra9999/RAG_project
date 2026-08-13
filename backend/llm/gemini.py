from langchain_google_genai import ChatGoogleGenerativeAI
from llm.base import BaseLLM


class GeminiLLM(BaseLLM):

    def __init__(
        self,
        api_key: str,
        model_name: str = "gemini-2.5-flash"
    ):

        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key
        )

    def generate(self, prompt: str) -> str:

        response = self.llm.invoke(prompt)

        return response.content