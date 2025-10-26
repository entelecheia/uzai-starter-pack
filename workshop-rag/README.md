# Workshop RAG Implementation

This directory contains a complete RAG (Retrieval-Augmented Generation) application following the workshop guide exactly. It uses Azure Functions with OpenAI bindings for simplified RAG orchestration.

## 🏗️ Architecture

This implementation uses the latest Azure Functions OpenAI bindings to create a powerful RAG pipeline with minimal code:

- **Frontend**: Static HTML/CSS/JavaScript with modern chat UI
- **Backend**: Azure Functions with OpenAI bindings
- **Search**: Azure AI Search for document retrieval
- **AI**: Azure OpenAI for text generation

## 📁 Directory Structure

```
workshop-rag/
├── backend-functions/          # Python Azure Functions implementation
│   ├── function_app.py         # Main function with RAG logic
│   ├── requirements.txt        # Python dependencies
│   ├── host.json              # Function app configuration
│   └── local.settings.json.example
├── backend-functions-csharp/   # C# Azure Functions implementation
│   ├── ChatFunction.cs         # Main function with RAG logic
│   ├── Program.cs              # Function app startup
│   ├── WorkshopRAG.csproj      # C# project file
│   ├── host.json               # Function app configuration
│   └── local.settings.json.example
├── frontend/                   # Static web app frontend
│   ├── index.html             # Main HTML page
│   ├── styles.css             # Modern CSS styling
│   └── app.js                 # JavaScript chat logic
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

1. Complete [Guide 01: Azure Account & Resource Setup](../README.md#guide-01-azure-account--resource-setup)
2. Complete [Guide 02: Local Development Environment Setup](../README.md#guide-02-local-development-environment-setup)

### Step 1: Choose Your Backend

You can use either Python or C# Azure Functions:

- **Python**: Easier for beginners, fewer dependencies
- **C#**: Better performance, more type safety

### Step 2: Configure Your Backend

1. Navigate to your chosen backend directory:
   ```bash
   cd workshop-rag/backend-functions        # For Python
   # OR
   cd workshop-rag/backend-functions-csharp # For C#
   ```

2. Copy the configuration template:
   ```bash
   cp local.settings.json.example local.settings.json
   ```

3. Edit `local.settings.json` and add your Azure keys:
   ```json
   {
     "IsEncrypted": false,
     "Values": {
       "AzureWebJobsStorage": "UseDevelopmentStorage=true",
       "FUNCTIONS_WORKER_RUNTIME": "python",  // or "dotnet-isolated" for C#
       "AZURE_OPENAI_CONNECTION_STRING": "endpoint=https://your-openai-resource.openai.azure.com/;key=your-openai-key;api-version=2024-02-15-preview",
       "AZURE_AI_SEARCH_CONNECTION_STRING": "endpoint=https://your-search-resource.search.windows.net;key=your-search-key;api-version=2024-02-01"
     },
     "Host": {
       "CORS": "*"
     }
   }
   ```

### Step 3: Install Dependencies

**For Python:**
```bash
cd workshop-rag/backend-functions
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**For C#:**
```bash
cd workshop-rag/backend-functions-csharp
dotnet restore
```

### Step 4: Upload Data to Azure AI Search

Follow [Guide 04, Step 3](../README.md#step-3-upload-data-to-your-ai-search-index) to upload documents to your search index.

### Step 5: Run the Application

1. Install the Azure Static Web Apps CLI:
   ```bash
   npm install -g @azure/static-web-apps-cli
   ```

2. Run the application:
   ```bash
   # From the repository root
   swa start workshop-rag/frontend --api-location workshop-rag/backend-functions
   # OR for C#
   swa start workshop-rag/frontend --api-location workshop-rag/backend-functions-csharp
   ```

3. Open your browser to `http://localhost:4280`

## 🔧 How It Works

### The Magic of OpenAI Bindings

This implementation uses Azure Functions OpenAI bindings to simplify RAG:

```python
@app.semantic_search_input(
    connection="AZURE_AI_SEARCH_CONNECTION_STRING",
    index_name="hackathon-index",
    query="{query}",
    top_k=5
)
@app.text_completion_input(
    connection="AZURE_OPENAI_CONNECTION_STRING",
    deployment_name="chat",
    max_tokens=500,
    temperature=0.7,
    system_prompt="You are a helpful assistant...",
    user_prompt="Context: {search_context}\n\nQuestion: {query}\n\nAnswer:"
)
def chat_function(req, search_context, completion):
    return completion
```

The bindings automatically:
1. **Search**: Query Azure AI Search for relevant documents
2. **Augment**: Combine the search results with the user's question
3. **Generate**: Send the augmented prompt to Azure OpenAI
4. **Return**: Send the generated response back to the frontend

### Frontend Features

- **Modern Chat UI**: Clean, responsive design with smooth animations
- **Real-time Messaging**: Instant responses with loading states
- **Error Handling**: Graceful error messages for debugging
- **Mobile Friendly**: Works on all device sizes

## 🛠️ Customization

### Changing the AI Behavior

Edit the `system_prompt` in your function to change how the AI responds:

```python
system_prompt="You are a helpful assistant that answers questions based on the provided context. Use the context to provide accurate and relevant answers. If the context doesn't contain enough information to answer the question, say so politely."
```

### Adjusting Search Parameters

Modify the search behavior by changing the `SemanticSearchInput` parameters:

```python
@app.semantic_search_input(
    connection="AZURE_AI_SEARCH_CONNECTION_STRING",
    index_name="hackathon-index",
    query="{query}",
    top_k=5  # Number of documents to retrieve
)
```

### Styling the Frontend

Edit `frontend/styles.css` to customize the appearance:

```css
:root {
  --primary-color: #667eea;
  --secondary-color: #764ba2;
  --background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
}
```

## 🐛 Troubleshooting

### Common Issues

1. **401 Unauthorized**: Check your connection strings in `local.settings.json`
2. **CORS Errors**: Ensure `"CORS": "*"` is in your `host.json`
3. **No Search Results**: Verify your Azure AI Search index has data
4. **Function Not Found**: Make sure you're running from the correct directory

### Debug Mode

Enable detailed logging by setting the log level in your `local.settings.json`:

```json
{
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AZURE_OPENAI_CONNECTION_STRING": "...",
    "AZURE_AI_SEARCH_CONNECTION_STRING": "...",
    "Logging__LogLevel__Default": "Debug"
  }
}
```

## 📚 Next Steps

1. **Add More Documents**: Upload more files to your Azure AI Search index
2. **Customize Prompts**: Experiment with different system prompts
3. **Deploy to Azure**: Follow the Azure deployment guide
4. **Add Features**: Implement conversation history, file upload, etc.

## 🔗 Related Resources

- [Azure Functions OpenAI Bindings Documentation](https://learn.microsoft.com/azure/azure-functions/functions-bindings-openai)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/)
- [Workshop Guide](../README.md#getting-started-onboarding-guides)
