# Prompt Engineering Module

This module explores structured prompt design patterns, evaluation workflows, and responsible AI guardrails for Azure OpenAI.

## Contents
- Prompt templates and prompt flow definitions
- Evaluation notebooks for iterative refinement
- Guardrail samples (content filters, safety heuristics)

## Setup
```bash
pip install -r requirements.txt
jupyter lab
```

Set the following variables before running notebooks:
```bash
export OPENAI_API_KEY="sk-your-openai-key"
export AZURE_OPENAI_ENDPOINT="https://<your-resource-name>.openai.azure.com/"
export AZURE_OPENAI_KEY="your-azure-openai-key"
```

## Next Steps
Proceed to the [RAG module](../rag/README.md) to combine your prompts with domain-specific data.
