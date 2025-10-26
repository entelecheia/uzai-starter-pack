# UzAI Starter Pack

Welcome to the UzAI Starter Pack, a pre-onboarding repository for the AI Hackathon. This guide walks you through the overall repository structure, prerequisites, environment setup, and how each learning module fits together so you can accelerate your build on Azure OpenAI.

## Repository Purpose

This repository is organized as a collection of focused modules that teach you how to design prompts, build retrieval-augmented generation (RAG) pipelines, deploy workloads to Azure, and ship a polished frontend. You can work through each module independently or follow them sequentially to evolve a single end-to-end application.

## Prerequisites

Before you begin, confirm you have the following:

- **Python 3.10+** for backend notebooks, RAG pipelines, and automation scripts.
- **Node.js 18+** (with npm or yarn) for running the frontend and any TypeScript tooling.
- **Azure subscription and Azure OpenAI access** to provision cognitive services, deploy models, and secure keys.
- (Optional) **Docker** if you prefer container-based development or deployment.

> Tip: If you are unsure which versions are currently installed, run `python --version` and `node --version` locally.

## Quick Start

Follow these steps to clone the repository, install dependencies, and configure environment variables.

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-org>/uzai-starter-pack.git
   cd uzai-starter-pack
   ```

2. **Set up Python dependencies**
   - Create and activate a virtual environment (recommended):
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # Windows: .venv\Scripts\activate
     ```
   - Install module-specific requirements once you enter each folder (see module READMEs for details). A common pattern is:
     ```bash
     pip install -r requirements.txt
     ```

3. **Install Node.js packages (for frontend tooling)**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

4. **Configure environment variables**
   - Create a `.env` file at the repository root (or within each module as instructed) and populate it with your secrets:
     ```bash
     OPENAI_API_KEY="sk-your-openai-key"
     AZURE_OPENAI_ENDPOINT="https://<your-resource-name>.openai.azure.com/"
     AZURE_OPENAI_KEY="your-azure-openai-key"
     AZURE_SEARCH_ENDPOINT="https://<your-search-resource>.search.windows.net/"
     AZURE_SEARCH_KEY="your-azure-search-key"
     ```
   - Export these variables in your shell when running scripts locally:
     ```bash
     export $(grep -v '^#' .env | xargs)
     ```

5. **Run sample apps (optional)**
   - Prompt engineering notebooks are typically executed via `jupyter lab` or `python <script>.py`.
   - RAG pipelines can be launched with `python app.py` or via Azure Functions as described in their module README.
   - The frontend can be started from its directory with:
     ```bash
     npm run dev
     ```
   - Azure deployment samples may require provisioning resources via the Azure CLI:
     ```bash
     az login
     az deployment group create --resource-group <rg> --template-file infra/main.bicep
     ```

## Module Overview

| Module | Description | Key Technologies |
| --- | --- | --- |
| [Prompt Engineering](prompt-engineering/README.md) | Learn structured prompting patterns, evaluation workflows, and guardrail techniques. | Jupyter, Python, Azure OpenAI, Prompt Flow |
| [Retrieval-Augmented Generation (RAG)](rag/README.md) | Build ingestion pipelines, vector indexes, and orchestrated RAG services that plug into Azure Cognitive Search. | Python, Azure AI Search, Azure Storage |
| [Azure Deployment](azure-deployment/README.md) | Package services for Azure hosting, configure CI/CD, and manage infrastructure as code. | Azure CLI, Bicep/ARM, GitHub Actions |
| [Frontend](frontend/README.md) | Deliver a responsive client that consumes your APIs or Azure OpenAI endpoints with rich UX. | React, TypeScript, Tailwind CSS |

## How the Modules Connect

1. **Prompt Engineering** lays the foundation by teaching you how to craft, evaluate, and iterate on prompts. The artifacts and best practices developed here are used throughout the rest of the repository.
2. **RAG** extends prompt engineering by injecting domain-specific knowledge using Azure Cognitive Search or other vector stores. Prompts defined in the first module are combined with retrieved context before being sent to Azure OpenAI endpoints.
3. **Azure Deployment** takes the services refined in the RAG module and shows you how to provision the necessary Azure resources, secure secrets, and set up deployment pipelines. This module references prompt and RAG assets to ensure a consistent deployment story.
4. **Frontend** consumes the APIs or Azure Function endpoints deployed earlier, providing an interactive interface for end users. It illustrates how to surface prompt or RAG improvements to the UI, enabling feedback loops back to the earlier modules.

Working through the modules sequentially yields an end-to-end application: start by designing prompts, integrate structured retrieval, deploy the services to Azure, and finally expose them through the frontend experience.

## Navigating the Repository

- Each module lives in its own directory with a dedicated README containing setup steps, architecture diagrams, and reference implementations.
- Shared assets (such as environment templates or utilities) reside in a future `common/` directory; refer to module READMEs for any additional dependencies.
- Use the module READMEs for detailed commands, notebook instructions, and deployment variations tailored to their respective scopes.

## Support and Contributions

- Open issues or feature requests via the repository's issue tracker.
- Submit pull requests following the module-specific contribution guidelines.
- For Azure-specific help, consult the [Azure OpenAI documentation](https://learn.microsoft.com/azure/ai-services/openai/) and the [Azure AI Search docs](https://learn.microsoft.com/azure/search/).

Happy building!
