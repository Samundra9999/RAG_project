from vector_store.chromadb.chromadb import ChromaDB

def get_vectorstore(store_type="chroma"):
    if store_type == "chroma":
        return ChromaDB()

    raise ValueError("Unsupported vector store")