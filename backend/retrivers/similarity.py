from retrivers.base import BaseRetriever


class VectorRetriever(BaseRetriever):

    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query: str, k: int = 5):
        return self.vector_store.similarity_search(query=query, k=k)