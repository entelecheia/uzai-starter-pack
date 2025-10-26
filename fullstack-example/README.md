# Fullstack Example

A complete FastAPI-based RAG (Retrieval-Augmented Generation) application with Azure AI Search and OpenAI integration. This implementation provides more control over the RAG pipeline compared to the Azure Functions approach.

## 🏗️ Architecture

- **Backend**: FastAPI with Azure AI Search and Azure OpenAI integration
- **Frontend**: React-based chat interface (reuses frontend-template)
- **Search**: Azure AI Search for document retrieval
- **AI**: Azure OpenAI for text generation
- **Deployment**: Docker containerization for Azure Container Apps

## 🚀 Quick Start

### Prerequisites

1. Complete [Guide 01: Azure Account & Resource Setup](../README.md#guide-01-azure-account--resource-setup)
2. Python 3.10+ installed
3. Docker (optional, for containerized deployment)

### Backend Setup

1. **Navigate to the backend directory:**
   ```bash
   cd fullstack-example/backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   ```bash
   cp env.example .env
   # Edit .env with your Azure keys
   ```

5. **Start the backend:**
   ```bash
   uvicorn backend.app:app --reload
   ```

The API will be available at `http://localhost:8000` with interactive docs at `http://localhost:8000/docs`.

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd fullstack-example/frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173`.

## 🔧 API Endpoints

### Chat Endpoint
```http
POST /api/chat
Content-Type: application/json

{
  "message": "What is RAG?"
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "query": "What is RAG?",
    "response": "RAG (Retrieval-Augmented Generation) is...",
    "context_used": "Retrieved document content...",
    "documents_found": 3,
    "generated_at": "2024-01-01T12:00:00.000Z",
    "source": "fullstack-example-rag"
  }
}
```

### Search Endpoint
```http
GET /api/search/{query}?top_k=5
```

**Response:**
```json
{
  "query": "RAG",
  "documents": [
    {
      "content": "Document content...",
      "title": "Document title",
      "score": 0.95
    }
  ],
  "count": 1
}
```

## 🐳 Docker Deployment

### Build and Run Locally

```bash
# Build the backend
docker build -t rag-backend ./backend

# Run the backend
docker run -p 8000:8000 --env-file ./backend/.env rag-backend
```

### Docker Compose

```bash
# Run both frontend and backend
docker-compose up --build
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `AZURE_SEARCH_ENDPOINT` | Azure AI Search endpoint URL | Yes |
| `AZURE_SEARCH_KEY` | Azure AI Search API key | Yes |
| `AZURE_SEARCH_INDEX_NAME` | Search index name (default: hackathon-index) | No |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint URL | Yes |
| `AZURE_OPENAI_KEY` | Azure OpenAI API key | Yes |
| `AZURE_OPENAI_DEPLOYMENT_NAME` | OpenAI deployment name (default: chat) | No |

### Customization

#### Adjusting Search Parameters

Edit `backend/services.py` to modify search behavior:

```python
def search_documents(self, query: str, top_k: int = 5) -> List[Dict]:
    # Change top_k to retrieve more/fewer documents
    # Add filters, scoring profiles, etc.
```

#### Modifying AI Behavior

Update the system prompt in `backend/services.py`:

```python
system_prompt = """Your custom system prompt here..."""
```

## 🆚 Comparison with Workshop RAG

| Feature | Fullstack Example | Workshop RAG |
|---------|------------------|--------------|
| **Backend** | FastAPI | Azure Functions |
| **Control** | Full control over RAG pipeline | Simplified with bindings |
| **Deployment** | Docker + Container Apps | Serverless Functions |
| **Customization** | High | Medium |
| **Learning Curve** | Steeper | Gentler |
| **Production Ready** | Yes | Yes (with limitations) |

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`
2. **Azure Connection Errors**: Verify your environment variables are correct
3. **CORS Errors**: The backend includes CORS middleware, but check your frontend URL
4. **Search Returns No Results**: Ensure your Azure AI Search index has data

### Debug Mode

Enable detailed logging by setting the log level:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Next Steps

1. **Add Authentication**: Implement user authentication and authorization
2. **Add File Upload**: Create endpoints for uploading documents to the search index
3. **Add Conversation History**: Store and retrieve chat history
4. **Add Monitoring**: Implement Application Insights or similar monitoring
5. **Deploy to Azure**: Use Azure Container Apps or Azure App Service

## 🔗 Related Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [Docker Documentation](https://docs.docker.com/)
