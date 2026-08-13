from langchain_community.document_loaders import PyPDFLoader
from loaders.base import BaseLoader
from loaders.document import Document

class PDFLoader(BaseLoader):

    def load(self, file_path):
        loader = PyPDFLoader(file_path=file_path)
        pages = loader.load()

        return [
            Document(
                page_content= page.page_content,
                metadata={
                    "source":file_path,
                    "page_no":i
                }
            )
            for i, page in enumerate(pages)
        ]