from chunking.recursive import RecursiveChunker

def get_chunker(chunk_type: str, config=None):

    chunkers = {
        "recursive": RecursiveChunker
    }

    if chunk_type not in chunkers:
        raise ValueError("Unsupported chunker")

    cls = chunkers[chunk_type]

    return cls(
        chunk_size=config.get("chunk_size", 1000),
        overlap=config.get("overlap", 200)
    )