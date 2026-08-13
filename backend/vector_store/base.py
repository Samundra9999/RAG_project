from abc import ABC, abstractmethod

class VectorStore(ABC):

    @abstractmethod
    def add_documents(self, docs):
        pass

    @abstractmethod
    def similarity_search(self, query, k: int = 5):
        pass