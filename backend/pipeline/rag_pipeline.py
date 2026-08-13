from prompts.rag_prompt import build_rag_prompt


class RAGPipeline:

    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def ask(self, query: str, k: int = 5):

        # 1. Retrieve docs
        docs = self.retriever.retrieve(query, k=k)

        # DEBUG (VERY IMPORTANT)
        print("\n===== RETRIEVED DOCS =====")
        for i, d in enumerate(docs):
            print(f"\n--- DOC {i} ---")
            print(d.page_content)
            print(d.metadata)

        # 2. Build context (THIS IS CRITICAL FIX)
        context = "\n\n".join(d.page_content for d in docs if d.page_content)

        # 3. Build prompt
        prompt = build_rag_prompt(
            context=context,
            question=query
        )

        # 4. Generate answer
        response = self.llm.generate(prompt)

        return {
            "query": query,
            "answer": response,
            "context": context,
            "sources": [d.metadata for d in docs]
        }