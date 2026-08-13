from langchain_huggingface import HuggingFaceEmbeddings
from embedding.base import BaseEmbedding


class HuggingfaceEmbed(BaseEmbedding):

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self._model = HuggingFaceEmbeddings(model_name=model_name)

    # expose required methods for Chroma

    def embed_documents(self, texts):
        return self._model.embed_documents(texts)

    def embed_query(self, text):
        return self._model.embed_query(text)