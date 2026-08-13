from embedding.base import BaseEmbedding
from embedding.huggingface import HuggingfaceEmbed

providers = {
    "huggingface":HuggingfaceEmbed
}

def get_embedding(provider_name:str)-> BaseEmbedding:
    provider_name = provider_name.lower()
    if provider_name not in providers:
        raise ValueError(f"No such provider... Available providers\n {list(providers.keys())}")
    
    return providers[provider_name]()