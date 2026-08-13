from loaders.pdf_loader import PDFLoader
from loaders.text_loader import TextLoader

def get_loader(file_path: str):
    if file_path.endswith(".pdf"):
        return PDFLoader()

    elif file_path.endswith(".txt"):
        return TextLoader()

    else:
        raise ValueError("Unsupported file type. Only PDF and TXT supported.")