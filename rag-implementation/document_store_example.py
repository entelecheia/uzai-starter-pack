"""Minimal retriever example used in onboarding."""

from pathlib import Path
from typing import List

import yaml

DATA_DIR = Path(__file__).parent / "data" / "knowledge_base"
CONFIG_PATH = Path(__file__).parent / "rag_config.yaml"


def load_documents() -> List[str]:
    """Load plain-text files from the knowledge base directory."""
    documents = []
    for file_path in sorted(DATA_DIR.glob("*.txt")):
        documents.append(file_path.read_text(encoding="utf-8"))
    return documents


def load_config() -> dict:
    if CONFIG_PATH.exists():
        return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    return {"embedding_model": "text-embedding-3-small", "chunk_size": 512}


def main() -> None:
    config = load_config()
    docs = load_documents()
    print(f"Loaded {len(docs)} documents with config: {config}")


if __name__ == "__main__":
    main()
