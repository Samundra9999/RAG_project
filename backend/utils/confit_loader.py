import yaml

def load_config(path=r"D:\Projects\RAG\config\config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)