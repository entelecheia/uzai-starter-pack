# Azure AI RAG Chatbot Workshop

This repository is the official starter kit for [Event Name] participants. Its goal is to help you skip the boring setup and get straight to the core of building an intelligent "Chat with your data" application using Generative AI.

It contains all the starter code, documentation, and links you need to get ready. Completing the "Pre-Onboarding" steps before the event will ensure you spend your valuable time building and innovating, not troubleshooting installations.

## 🚀 What We're Building

We will be building a Retrieval-Augmented Generation (RAG) application. In simple terms, RAG is an app that lets you "talk" to your own private documents.

- **Without RAG**: An AI model like GPT-4 only knows what it was trained on. It knows nothing about your specific PDF file or company data.
- **With RAG**: We use a "Retriever" (Azure AI Search) to find relevant information from your data first, and then "Augment" (enrich) the model's knowledge with this information before it generates a response.

This is the core architecture for thousands of modern AI applications, and you'll build one yourself in this workshop.

## 🛠️ The Tech Stack

This project uses a modern, serverless "fullstack" architecture on Azure. The badges below represent the core technologies we'll use and link to their documentation.

[![Static Web Apps](https://img.shields.io/badge/Static_Web_Apps-0078D7?style=for-the-badge&logo=azure-static-web-apps&logoColor=white)](https://azure.microsoft.com/en-us/products/static-web-apps)
[![Azure AI Search](https://img.shields.io/badge/Azure_AI_Search-0078D7?style=for-the-badge&logo=azure-search&logoColor=white)](https://azure.microsoft.com/en-us/products/ai-services/cognitive-search)
[![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

| Service | Role in Project |
|---------|----------------|
| Azure Static Web Apps | Hosts our frontend (HTML/CSS/JavaScript) and makes it accessible worldwide |
| Azure Functions | Acts as our serverless backend API. This is the "brain" of our app |
| Azure OpenAI Service | Gives us access to powerful Large Language Models (LLMs) like GPT-3.5-Turbo or GPT-4 |
| Azure AI Search | This is our "Retriever." It's used to index our data and perform lightning-fast vector and semantic search |

## 🎯 Learning Objectives

By completing this onboarding and building the starter project, you will be able to:

- Provision a complete AI app infrastructure on Azure
- Explain the Retrieval-Augmented Generation (RAG) architecture
- Implement a serverless API endpoint (Azure Functions)
- Use the new Azure Functions OpenAI Bindings to simplify your RAG orchestration
- Connect a simple frontend (Static Web Apps) to a backend API
- Troubleshoot common issues in cloud-native applications

## 📚 Getting Started: Onboarding Guides

Please follow these guides in order. It is critical that you complete Guides 1 and 2 before the event.

### Guide 01: Azure Account & Resource Setup

Welcome to the first hands-on step! In this guide, we'll create a free Azure account and provision (create) the 4 core services needed for our RAG application.

**Estimated Time: 30 minutes**

#### Step 1: Create a Free Azure Account

You have two main options for a free account.

**Option A: Azure for Students (Recommended)**
- If you are a student at an eligible educational institution, this is your best option.
- No credit card required
- You get $100 in free credit
- Link: [azure.microsoft.com/free/students](https://azure.microsoft.com/free/students)
- This process requires you to verify your school email address

**Option B: Azure Free Trial**
- If you are not a student, you can use the standard free trial.
- A credit card is required (you will not be charged unless you manually upgrade your account)
- You get $200 in credit to use for 30 days
- Link: [azure.microsoft.com/free](https://azure.microsoft.com/free)

#### Step 2: Sign in to the Azure Portal

Once your account is active, sign in at [portal.azure.com](https://portal.azure.com).

The Portal is your graphical dashboard for managing all your Azure resources. We'll use this to create our 4 services.

#### Step 3: Provision the 4 Core Services

We need to create 4 services in total. The important things to pay attention to are the Region (choose one close to you, e.g., "West Europe" or "North Europe") and the Pricing tier (always choose "Free" or "Basic" if available).

**Service 1: Azure OpenAI Service**
This gives us access to the AI models.

1. In the top search bar, type "Azure OpenAI" and select it.
2. Click "Create".
3. Fill out the form:
   - Subscription: Select your Azure subscription (e.g., "Azure for Students")
   - Resource Group: Click "Create new" and give it a unique name, like `rg-ai-hackathon`. (A resource group is just a folder to organize services)
   - Region: Choose a region (e.g., "North Europe" or "Sweden Central"). Note: Not all regions have all models. Sweden Central is a good choice
   - Name: Give it a globally unique name, like `oai-[yourname]-hackathon`
   - Pricing tier: Select Standard S0
4. Click "Review + submit", then "Create".

**TASK: Deploy Models**
Once the OpenAI service is created (it may take a few minutes), you must:

1. Click "Go to resource"
2. On the left menu, select "Model deployments" (under Resource Management)
3. Click "Manage Deployments". This will open Azure AI Studio
4. You need to deploy two models:
   - **For Generation**: Click "Create new deployment"
     - Select model: `gpt-35-turbo` (or `gpt-4` if available)
     - Deployment name: `chat` (use this exact name)
   - **For Embeddings**: Click "Create new deployment"
     - Select model: `text-embedding-ada-002`
     - Deployment name: `embedding` (use this exact name)

**Service 2: Azure AI Search**
This will be our "memory" (vector database).

1. In the top search bar, type "AI Search" and select it.
2. Click "Create".
3. Fill out the form:
   - Subscription: Select your subscription
   - Resource Group: Select the same group you just made (`rg-ai-hackathon`)
   - Service Name: Give it a globally unique name, like `search-[yourname]-hackathon`
   - Region: Select the same region as your OpenAI service
   - Pricing tier: Select Basic or Standard. (The free F tier does not always support the features we need. Basic is the safest bet for the hackathon and should be covered by your credits)
4. Click "Review + submit", then "Create".

**Service 3: Azure Function App**
This will be our backend API.

1. In the top search bar, type "Function App" and select it.
2. Click "Create".
3. Fill out the form:
   - Subscription: Select your subscription
   - Resource Group: Select `rg-ai-hackathon`
   - Function App Name: Give it a globally unique name, like `func-[yourname]-hackathon`
   - Publish: Select Code
   - Runtime stack: Set this to Python or .NET depending on your backend choice. Don't worry, you can change this later. (We recommend Python 3.10 or .NET 8)
   - Region: Select the same region again
   - Operating System: Select Linux (cheaper and more common)
   - Plan: Select Consumption (Serverless). This is extremely cheap (practically free for our usage)
4. Click "Review + submit", then "Create".

**Service 4: Azure Static Web App**
This will be our frontend host.

1. In the top search bar, type "Static Web Apps" and select it.
2. Click "Create".
3. Fill out the form:
   - Subscription: Select your subscription
   - Resource Group: Select `rg-ai-hackathon`
   - Name: Give it a unique name, like `swa-[yourname]-hackathon`
   - Plan: Select Free
   - Region: Select a region (e.g., "West Europe")
   - Deployment details: Select Other. (We won't connect it to GitHub just yet)
4. Click "Review + submit", then "Create".

#### Step 4: Collect Your Keys and Endpoints

Our code needs "keys" to access these services. We need to collect these in a safe place on our computer (like a temporary notepad file). **NEVER share these keys with anyone.**

You can find your services easily by navigating to your resource group (`rg-ai-hackathon`) in the Azure Portal.

| Service | Key/Endpoint | Where to find it |
|---------|--------------|------------------|
| Azure OpenAI | `AZURE_OPENAI_ENDPOINT` | Go to your OpenAI service. Under "Resource Management", select "Keys and Endpoint". Copy the "Endpoint" value |
| Azure OpenAI | `AZURE_OPENAI_KEY` | On the same page, copy "KEY 1" |
| Azure AI Search | `AZURE_AI_SEARCH_ENDPOINT` | Go to your AI Search service. On the "Overview" page, copy the "Url" (should look like https://...search.windows.net) |
| Azure AI Search | `AZURE_AI_SEARCH_KEY` | Go to your AI Search service. Under "Settings", select "Keys". Copy the "Primary admin key" |

Congratulations! Your cloud infrastructure is now ready. You have all 4 services you need and the 4 secret values to connect your code to them.

### Guide 02: Local Development Environment Setup

Now that we have our Azure resources in the cloud, we need to set up our local machine to develop and "talk" to them.

**Estimated Time: 20 minutes**

This starter kit is designed to be developed with Visual Studio Code (VS Code), a free and powerful code editor.

#### Step 1: Install Visual Studio Code

If you don't already have it, download and install VS Code.
- Download: [code.visualstudio.com](https://code.visualstudio.com)

#### Step 2: Install Required Runtimes

You need to install the "runtime" (language) you'll be using for your backend. You only need to install ONE of these.

**For Python Developers:**
- Install Python 3.10 (or 3.11)
- Download: [python.org/downloads](https://python.org/downloads)
- Important: During installation on Windows, make sure to check the box that says "Add Python to PATH"

**For .NET (C#) Developers:**
- Install the .NET 8 SDK
- Download: [dotnet.microsoft.com/download/dotnet/8.0](https://dotnet.microsoft.com/download/dotnet/8.0)

#### Step 3: Install Azure Functions Core Tools

This is a command-line tool that lets you run and debug Azure Functions on your local machine. It's essential for our development.

The easiest way to install it is using npm (the Node.js package manager), which comes with Node.js.

1. Install Node.js (if you don't have it):
   - Download the LTS version from [nodejs.org](https://nodejs.org). This will install npm with it.
2. Install the Core Tools:
   - Open a new terminal (Terminal, PowerShell, or CMD)
   - Run the following command:
     ```bash
     npm install -g azure-functions-core-tools@4
     ```
3. Verify installation:
   - Run `func --version`. You should see a 4.x.x.x version.

#### Step 4: Install VS Code Extensions

Extensions give VS Code "superpowers." Open VS Code, go to the "Extensions" tab (the square icon in the sidebar), and install the following:

- **Azure Functions** (ID: `ms-azuretools.vscode-azurefunctions`)
  - Why: Lets you run, debug, and deploy Function apps directly from VS Code
- **Azure Static Web Apps** (ID: `ms-azuretools.vscode-azurestaticwebapps`)
  - Why: Helps you run the frontend and backend together and deploy them
- **(Optional) Python Extension** (ID: `ms-python.python`)
  - Why: Essential if you are developing in Python (syntax highlighting, debugging, etc.)
- **(Optional) C# Dev Kit** (ID: `ms-dotnettools.csdevkit`)
  - Why: Essential if you are developing in .NET (syntax highlighting, debugging, etc.)

#### Step 5: Clone This Repository

Now, clone this code repository (the one you're likely reading in your browser) to your local machine.

1. Open your terminal
2. Navigate to where you store your projects (e.g., Documents or Code)
3. Run the git clone command (replace the URL with this repo's URL):
   ```bash
   git clone https://github.com/entelecheia/uzai-starter-pack.git
   ```
4. Open the cloned folder in VS Code:
   ```bash
   cd uzai-starter-pack
   code .
   ```

Congratulations! Your local environment is now fully set up. You have VS Code, the correct runtime, the Azure tools, and the code.

### Guide 03: Understanding the Application Architecture (RAG)

Before we run the code, let's look at exactly what we're building. This architecture is called Retrieval-Augmented Generation (RAG).

**Estimated Time: 10 minutes**

#### The Problem

A standard Large Language Model (LLM) like GPT-4 is very smart, but its knowledge is "frozen" in time. It doesn't know about the world after its training cutoff (e.g., 2023), and it definitely doesn't know about your private data (e.g., your company handbook, project PDFs, or emails).

If you ask it, "How many vacation days do I get?" it will say, "I'm sorry, I don't have access to your personal information."

#### The Solution: Retrieval-Augmented Generation (RAG)

RAG solves this by giving the model a real-time "memory" and "context." Instead of just asking the model a question, we follow a 2-step process:

1. **Retrieval**: Before we ask the AI, we first search our own database (Azure AI Search) for information relevant to the question.
   - Question: "How many vacation days do I get?"
   - Search: We search our "employee_handbook.pdf" index and find the text chunk: "All full-time employees receive 25 days of paid vacation per year."

2. **Augmentation & Generation**: Now, we take the user's question AND the data we just found and augment (enrich) it. We send this new, improved "prompt" to the AI.
   - Old Prompt (Bad): "How many vacation days do I get?"
   - New Prompt (Good): "Using the following context: 'All full-time employees receive 25 days of paid vacation per year.' Now, answer this question: How many vacation days do I get?"

The model will now happily answer, "According to your employee handbook, you receive 25 days of paid vacation per year."

#### Data Flow in Our Project

This diagram shows how data flows in the app you're about to build:

![Architecture Diagram](https://via.placeholder.com/600x300.png?text=Architecture+Diagram)

1. **Frontend (Static Web App)**: User types "What is RAG?" into the chat box
2. **API Request**: The frontend sends a fetch request to our API endpoint (`/api/chat`)
3. **Backend (Azure Function)**: Our chat function receives the request
4. **Where the Magic Happens**: Instead of writing complex orchestration code, we use the Azure Functions OpenAI Bindings:
   - `SemanticSearchInput`: This "input binding" automatically takes the user's question ("What is RAG?"), sends it to Azure AI Search, finds the most relevant documents (e.g., from this guide), and stores them in a variable called `context`
   - `TextCompletionInput`: This "input binding" takes the same query, combines it with the context we just retrieved, and sends it all to Azure OpenAI to generate an answer, which it returns in a variable called `result`
5. **API Response**: The function returns OpenAI's answer back to the frontend
6. **Frontend (Static Web App)**: The chat window updates with the intelligent answer

The use of these "bindings" is key to this hackathon. It allows us to build a very powerful RAG pipeline with a surprisingly small amount of code, which is perfect for rapid prototyping.

### Guide 04: Running the Starter Project

This is the final step! Let's get the code running locally. We need to run two things at once:
- The Backend API (Python or .NET)
- The Frontend Web App (JavaScript)

The easiest way to do this is with the Azure Static Web Apps CLI, which handles all of this for us.

**Estimated Time: 15 minutes**

#### Step 1: Choose Your Backend Path

You only need to choose one backend. In VS Code, open the `workshop-rag/` folder. You will see:
- `backend-functions/` (Python Azure Functions)
- `backend-functions-csharp/` (.NET Azure Functions)
- `frontend/`

Decide if you want to run the Python backend or the .NET backend.

#### Step 2: Create Your Own local.settings.json

This is the most important step.

For security, the file with your secret keys (`local.settings.json`) is ignored by Git (`.gitignore`). You must create this file yourself from the template provided.

1. Navigate into your chosen backend folder (e.g., `workshop-rag/backend-functions/` or `workshop-rag/backend-functions-csharp/`)
2. You will see a file named `local.settings.json.example`
3. Copy and rename this file to `local.settings.json` (remove the `.example`)
4. Open your new `local.settings.json`
5. Now, paste in the 4 values you collected in Guide 01

Important: If you are using the C# backend, change `FUNCTIONS_WORKER_RUNTIME` to "dotnet-isolated".

The `"Host": { "CORS": "*" }` has been added so your local frontend can call your local backend without security errors (CORS errors).

#### Step 3: Upload Data to Your AI Search Index

A RAG app needs data to talk to! We haven't built a file upload feature yet, so let's manually upload this README.md file to our search index.

1. In the Azure Portal, navigate to your Azure AI Search service
2. Click the "Import data" button at the top
3. Data Source: Select "Upload files (preview)"
4. Upload: Drag the `docs/GUIDE_03_APPLICATION_ARCHITECTURE.md` file from this repository into the upload area
5. Content extraction: Leave settings as default
6. Add AI enrichment: Skip this step for now (click "Skip to...")
7. Customize target index:
   - Index name: `hackathon-index` (must match your `local.settings.json`)
   - Make sure the content field has "Retrievable" and "Searchable" checked
8. Create an indexer:
   - Indexer Name: `hackathon-indexer`
9. "Submit" to start the indexing

After a minute or two, your AI Search service now contains the knowledge from our architecture guide.

#### Step 4: Run the App Locally

We will use the Azure Static Web Apps CLI (SWA CLI) to start both the frontend and backend at the same time.

1. Install the SWA CLI:
   ```bash
   npm install -g @azure/static-web-apps-cli
   ```

2. Run the App:
   - Open a terminal in the ROOT folder of this repository (the one containing `workshop-rag/`, `fullstack-example/`, etc.)
   - Run the command that matches your backend choice:
   
   **For Python Users:**
   ```bash
   swa start workshop-rag/frontend --api-location workshop-rag/backend-functions
   ```
   
   **For .NET (C#) Users:**
   ```bash
   swa start workshop-rag/frontend --api-location workshop-rag/backend-functions-csharp
   ```

The terminal will show a lot of output as it builds and starts the servers.

When it's ready, you'll see a message: "Azure Static Web Apps emulator is now running..."

Open your browser and go to `http://localhost:4280`.

You should now see the chat application!

**Test it**: Ask a question that it could only know from the data you uploaded. For example:
- "What is RAG?"
- "What is the purpose of SemanticSearchInput?"

If it answers correctly, Congratulations! You are running a fully working RAG application locally.

### Guide 05: Troubleshooting & FAQ

Running into problems is a normal part of development. Here is a list of the most common issues you might face and how to fix them.

#### Problem: "401 Unauthorized" or "Authentication failed"

**Symptom**: You ask a question in the chat, and it returns a red error. The terminal running `swa start` shows a 401 Unauthorized error.

**Cause**: This is almost always a problem with your API keys.

**Solution**:
1. Stop the `swa start` process (Ctrl+C)
2. Open your `local.settings.json` file (e.g., `workshop-rag/backend-functions/local.settings.json`)
3. Carefully check the 4 values you pasted in:
   - `AZURE_OPENAI_ENDPOINT`
   - `AZURE_OPENAI_KEY`
   - `AZURE_AI_SEARCH_ENDPOINT`
   - `AZURE_AI_SEARCH_KEY`
4. Make sure you didn't swap the OpenAI key and the AI Search key
5. Make sure there are no extra spaces or characters
6. Make sure the AI Search endpoint does not include a `/` at the end (Format: `https://...search.windows.net`)
7. Save the file and run `swa start`... again

#### Problem: "CORS error" in the browser console

**Symptom**: The chat app loads, but when you ask a question, nothing happens. You open the browser developer tools (F12) -> Console and see an error about "CORS" or "Cross-Origin Resource Sharing".

**Cause**: The frontend (`localhost:4280`) is not allowed to call the backend API (`localhost:7071`).

**Solution**:
1. Stop the `swa start` process
2. Open your `local.settings.json` file
3. Make sure this block is at the bottom (inside the main `{...}`):
   ```json
   "Host": {
     "CORS": "*"
   }
   ```
4. Save and run `swa start`... again

#### Problem: "App build failed to produce artifact folder"

**Symptom**: Running `swa start`... crashes with an error like `App build failed to produce artifact folder: 'workshop-rag/frontend'`.

**Cause**: You are running the swa CLI from the wrong directory.

**Solution**:
1. Make sure your terminal is in the ROOT folder of this repository (the one containing `workshop-rag/`, `fullstack-example/`, etc.), not inside `workshop-rag/frontend/` or `workshop-rag/backend-functions/`
2. The command should be `swa start workshop-rag/frontend...` which tells it where the frontend code is relative to your current location

#### Problem: "Cannot find module 'azure-functions'" (Python)

**Symptom**: The Python function fails to start and complains about missing packages.

**Cause**: The Python dependencies aren't installed.

**Solution**:
1. Stop `swa start`
2. Create a virtual environment (recommended):
   ```bash
   cd workshop-rag/backend-functions
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
3. Install the packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Go back to the root folder (`cd ../..`) and run `swa start`... again

#### Problem: The response is "I don't know" (or a generic answer)

**Symptom**: The app works, but when you ask about your data (e.g., "What is RAG?"), it gives a generic answer instead of one from your documents.

**Cause**: The RAG process (the "Retrieval") is failing. This can have two causes:
1. Your data isn't in the index: Did you complete "Step 3: Upload Data" in Guide 4? Did you use the correct index name (`hackathon-index`)?
2. Your code is pointing to the wrong index: Double-check the `AZURE_AI_SEARCH_INDEX_NAME` in your `local.settings.json`. It must match the index name you created in the Azure portal (e.g., `hackathon-index`)

#### Problem: "func" or "swa" command not found

**Symptom**: You type `func --version` or `swa start` in your terminal and get an error like "command not found".

**Cause**: The tools didn't install correctly or your terminal's "PATH" hasn't updated.

**Solution**:
1. Restart your terminal. This fixes 90% of "PATH" issues. Restart VS Code as well
2. If that fails, try reinstalling the tools from Guide 02:
   ```bash
   npm install -g azure-functions-core-tools@4
   npm install -g @azure/static-web-apps-cli
   ```

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
