# Retrieval-Augmented Generation Implementation

This module demonstrates how to wire a lightweight document store, embedding pipeline, and query orchestrator together for grounded responses.

## Files

- `document_store_example.py` — command-line entry point that loads sample documents and prints the active configuration.
- `rag_config.yaml` — default hyperparameters for chunking, embeddings, and retriever selection.
- `data/knowledge_base/sample_article.txt` — example corpus used during onboarding.
- `resources/rag_tutorial.pdf` — printable walkthrough of the architecture for facilitator-led sessions.

## Quickstart

```bash
python document_store_example.py
```

The script expects the optional dependency `pyyaml`. Install it with `pip install pyyaml` if it is not already included in your environment.

## Next Steps

Pair this example with the Azure deployment samples to host the retrieval pipeline behind a serverless API.
