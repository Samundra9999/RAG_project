
from retrivers.similarity import VectorRetriever
from retrivers.bm25 import BM25Retriever
from retrivers.hybrid import HybridRetriever


def get_retriever(retriever_type: str, vector_store=None, docs=None):

    if retriever_type == "vector":
        return VectorRetriever(vector_store)

    if retriever_type == "bm25":
        return BM25Retriever(docs)

    if retriever_type == "hybrid":
        bm25 = BM25Retriever(docs)
        return HybridRetriever(vector_store, bm25)

    raise ValueError(f"Unknown retriever type: {retriever_type}")