from abc import ABC, abstractmethod
from typing import Dict
from loaders.document import Document

class Chunker(ABC):

    @abstractmethod
    def chunk(self, docs:list[Document]) -> list[Document]:
        pass