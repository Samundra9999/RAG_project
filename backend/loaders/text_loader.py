from langchain_community.document_loaders import TextLoader
from loaders.base import BaseLoader
from loaders.document import Document


class TextLoader(BaseLoader):

    def load(self, file_path):
        loader = TextLoader(file_path)
        pages = loader.load()

        return [

            Document(
                page_content=page.page_content,
                metadata={
                    "source":file_path
                }
            )
            for page in pages
        ]