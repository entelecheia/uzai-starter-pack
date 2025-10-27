# UzAI Starter Pack

Welcome to the UzAI Starter Pack, a comprehensive collection of modules for building AI-powered applications with Azure OpenAI and RAG (Retrieval-Augmented Generation) technology.

## 📖 For Workshop Participants

If you're attending the Azure AI RAG Chatbot Workshop, please start with the **[Workshop Guide](WORKSHOP_GUIDE.md)** for step-by-step instructions.

This README provides an overview of the entire repository structure and all available implementations.

## 🚀 What We're Building

This repository contains everything you need to build intelligent "Chat with your data" applications using Retrieval-Augmented Generation (RAG). RAG allows AI models to access and use your private documents, providing accurate, context-aware responses.

- **Without RAG**: AI models only know what they were trained on
- **With RAG**: AI models can access your documents and provide accurate, up-to-date information

## 🛠️ The Tech Stack

[![Static Web Apps](https://img.shields.io/badge/Static_Web_Apps-0078D7?style=for-the-badge&logo=azure-static-web-apps&logoColor=white)](https://azure.microsoft.com/en-us/products/app-service/static)
[![Azure AI Search](https://img.shields.io/badge/Azure_AI_Search-0078D7?style=for-the-badge&logo=azure-search&logoColor=white)](https://azure.microsoft.com/en-us/products/ai-services/cognitive-search)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

| Service | Role in Project |
|---------|----------------|
| Azure Static Web Apps | Hosts frontend applications worldwide |
| Azure Functions | Serverless backend API with OpenAI bindings |
| Azure OpenAI Service | Large Language Models (GPT-3.5, GPT-4) |
| Azure AI Search | Document retrieval and vector search |

## Choose Your Implementation Path

This repository provides two different approaches to building RAG applications:

### Option 1: Azure Functions + OpenAI Bindings (Workshop Style)
Located in `workshop-rag/` - This follows the workshop guide exactly with Azure Functions using the new OpenAI bindings for simplified RAG orchestration.

**Best for**: Learning the latest Azure patterns, serverless architecture, rapid prototyping

### Option 2: FastAPI + Traditional Integration (Fullstack Example)
Located in `fullstack-example/` - This uses FastAPI with traditional Azure SDK integration for more control over the RAG pipeline.

**Best for**: Production applications, custom business logic, microservices architecture

## UzAI Starter Pack

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
   git clone https://github.com/entelecheia/uzai-starter-pack.git
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
| [Workshop RAG](workshop-rag/README.md) | Complete Azure Functions RAG implementation with OpenAI bindings - follows the workshop guide exactly | Azure Functions, OpenAI Bindings, Azure AI Search, Static Web Apps |
| [Fullstack Example](fullstack-example/README.md) | FastAPI-based RAG implementation with traditional Azure SDK integration | FastAPI, Python, Azure AI Search, Docker |
| [Prompt Engineering](prompt-engineering/README.md) | Learn structured prompting patterns, evaluation workflows, and guardrail techniques. | Jupyter, Python, Azure OpenAI, Prompt Flow |
| [Retrieval-Augmented Generation (RAG)](rag/README.md) | Build ingestion pipelines, vector indexes, and orchestrated RAG services that plug into Azure Cognitive Search. | Python, Azure AI Search, Azure Storage |
| [Azure Deployment](azure-deployment/README.md) | Package services for Azure hosting, configure CI/CD, and manage infrastructure as code. | Azure CLI, Bicep/ARM, GitHub Actions |
| [Frontend](frontend/README.md) | Deliver a responsive client that consumes your APIs or Azure OpenAI endpoints with rich UX. | React, TypeScript, Tailwind CSS |

## How the Modules Connect

1. **Workshop RAG** provides a complete, ready-to-run implementation following the workshop guide. This is the fastest way to get a working RAG application using Azure Functions with OpenAI bindings.
2. **Fullstack Example** offers an alternative FastAPI-based implementation with more control over the RAG pipeline, ideal for production applications.
3. **Prompt Engineering** lays the foundation by teaching you how to craft, evaluate, and iterate on prompts. The artifacts and best practices developed here are used throughout the rest of the repository.
4. **RAG** extends prompt engineering by injecting domain-specific knowledge using Azure Cognitive Search or other vector stores. Prompts defined in the first module are combined with retrieved context before being sent to Azure OpenAI endpoints.
5. **Azure Deployment** takes the services refined in the RAG module and shows you how to provision the necessary Azure resources, secure secrets, and set up deployment pipelines. This module references prompt and RAG assets to ensure a consistent deployment story.
6. **Frontend** consumes the APIs or Azure Function endpoints deployed earlier, providing an interactive interface for end users. It illustrates how to surface prompt or RAG improvements to the UI, enabling feedback loops back to the earlier modules.

**Choose your path:**
- **Quick Start**: Use Workshop RAG for immediate results following the workshop guide
- **Deep Learning**: Work through Prompt Engineering → RAG → Azure Deployment → Frontend sequentially
- **Production Ready**: Use Fullstack Example as a foundation for custom business logic

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
