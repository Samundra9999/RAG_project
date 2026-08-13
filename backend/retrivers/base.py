# retriever/base.py

from abc import ABC, abstractmethod
from typing import List, Any


class BaseRetriever(ABC):

    @abstractmethod
    def retrieve(self, query: str, k: int = 5) -> List[Any]:
        pass