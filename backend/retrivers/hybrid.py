from retrivers.base import BaseRetriever


class HybridRetriever(BaseRetriever):

    def __init__(
        self,
        vector_store,
        bm25_retriever
    ):
        self.vector_store = vector_store
        self.bm25 = bm25_retriever

    def retrieve(self, query, k=5):

        vector_docs = self.vector_store.similarity_search(
            query=query,
            k=k
        )

        bm25_docs = self.bm25.retrieve(
            query=query,
            k=k
        )

        combined = []

        seen = set()

        for doc in vector_docs + bm25_docs:

            content = doc.page_content

            if content not in seen:
                seen.add(content)
                combined.append(doc)

        return combined[:k]