from langchain_chroma import Chroma
from langchain_core.documents import Document as LCDocument
from embedding.huggingface import HuggingfaceEmbed
from vector_store.base import VectorStore
import uuid


class ChromaDB(VectorStore):

    def __init__(self):
        self.embedder = HuggingfaceEmbed()

        self.store = Chroma(
            collection_name="rag",
            persist_directory=f"./db/{str(uuid.uuid4())}",
            embedding_function=self.embedder
        )

    def add_documents(self, docs):

        lc_docs = [
            LCDocument(
                page_content=d.page_content,
                metadata=d.metadata
            )
            for d in docs
        ]

        self.store.add_documents(
            documents=lc_docs,
            ids=[str(uuid.uuid4()) for _ in lc_docs]
        )

    def similarity_search(self, query, k=5):
        return self.store.similarity_search(query=query, k=k)