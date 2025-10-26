# Retrieval-Augmented Generation (RAG) Module

This module demonstrates how to ground your prompts with domain knowledge using Azure AI Search and vector databases.

## Contents
- Data ingestion notebooks and scripts
- Indexing utilities for Azure Cognitive Search or Azure AI Search
- API services that orchestrate retrieval and response synthesis

## Setup
```bash
pip install -r requirements.txt
python ingest.py
python app.py
```

Set environment variables before running services:
```bash
export OPENAI_API_KEY="sk-your-openai-key"
export AZURE_OPENAI_ENDPOINT="https://<your-resource-name>.openai.azure.com/"
export AZURE_OPENAI_KEY="your-azure-openai-key"
export AZURE_SEARCH_ENDPOINT="https://<your-search-resource>.search.windows.net/"
export AZURE_SEARCH_KEY="your-azure-search-key"
```

## Next Steps
After validating the pipeline locally, continue to the [Azure deployment module](../azure-deployment/README.md) to provision cloud resources.
