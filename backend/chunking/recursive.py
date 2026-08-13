from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chunking.base import Chunker


class RecursiveChunker(Chunker):

    def __init__(self, chunk_size=1000, overlap=200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=[
                "\n\n",   # sections
                "\n•",    # bullet points
                "\n", 
                ".", 
                ]
)

    def chunk(self, docs):
        chunks = []

        for doc in docs:
            texts = self.splitter.split_text(doc.page_content)

            for text in texts:
                chunks.append(
                    Document(
                        page_content=text,
                        metadata=doc.metadata.copy()
                    )
                )

        return chunks