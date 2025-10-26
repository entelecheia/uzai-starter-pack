from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging

from .services import rag_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="RAG Fullstack Demo",
    description="A FastAPI-based RAG application with Azure AI Search and OpenAI integration",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    status: str
    data: dict

@app.get("/")
def root():
    return {"message": "RAG Fullstack Demo API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "rag-fullstack-demo"}

@app.post("/api/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest) -> ChatResponse:
    """
    Chat endpoint that processes queries using RAG pipeline.
    
    This endpoint:
    1. Searches Azure AI Search for relevant documents
    2. Generates a response using Azure OpenAI with retrieved context
    3. Returns the response along with metadata
    """
    try:
        logger.info(f"Received chat request: {request.message}")
        
        # Process the query using RAG
        result = rag_service.process_query(request.message)
        
        return ChatResponse(
            status="success",
            data=result
        )
        
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )

@app.get("/api/search/{query}")
def search_documents(query: str, top_k: int = 5):
    """
    Search endpoint for testing document retrieval.
    
    This endpoint allows you to test the search functionality
    without going through the full RAG pipeline.
    """
    try:
        documents = rag_service.search_documents(query, top_k)
        return {
            "query": query,
            "documents": documents,
            "count": len(documents)
        }
    except Exception as e:
        logger.error(f"Error searching documents: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Search error: {str(e)}"
        )
