import os
import logging
from datetime import datetime
from typing import Dict, List, Optional
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RAGService:
    def __init__(self):
        # Azure AI Search configuration
        self.search_endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
        self.search_key = os.getenv("AZURE_SEARCH_KEY")
        self.search_index = os.getenv("AZURE_SEARCH_INDEX_NAME", "hackathon-index")
        
        # Azure OpenAI configuration
        self.openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.openai_key = os.getenv("AZURE_OPENAI_KEY")
        self.openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "chat")
        
        # Initialize clients
        self.search_client = None
        self.openai_client = None
        
        if self.search_endpoint and self.search_key:
            self.search_client = SearchClient(
                endpoint=self.search_endpoint,
                index_name=self.search_index,
                credential=AzureKeyCredential(self.search_key)
            )
        
        if self.openai_endpoint and self.openai_key:
            self.openai_client = AzureOpenAI(
                azure_endpoint=self.openai_endpoint,
                api_key=self.openai_key,
                api_version="2024-02-15-preview"
            )
    
    def search_documents(self, query: str, top_k: int = 5) -> List[Dict]:
        """Search for relevant documents using Azure AI Search"""
        if not self.search_client:
            logger.warning("Azure AI Search not configured")
            return []
        
        try:
            results = self.search_client.search(
                search_text=query,
                top=top_k,
                include_total_count=True
            )
            
            documents = []
            for result in results:
                documents.append({
                    "content": result.get("content", ""),
                    "title": result.get("title", ""),
                    "score": result.get("@search.score", 0)
                })
            
            logger.info(f"Found {len(documents)} documents for query: {query}")
            return documents
            
        except Exception as e:
            logger.error(f"Error searching documents: {str(e)}")
            return []
    
    def generate_response(self, query: str, context: str) -> str:
        """Generate a response using Azure OpenAI with retrieved context"""
        if not self.openai_client:
            logger.warning("Azure OpenAI not configured")
            return "I'm sorry, but I don't have access to AI services at the moment."
        
        try:
            system_prompt = """You are a helpful assistant that answers questions based on the provided context. 
            Use the context to provide accurate and relevant answers. If the context doesn't contain enough 
            information to answer the question, say so politely and suggest what information might be helpful."""
            
            user_prompt = f"""Context: {context}

Question: {query}

Answer:"""
            
            response = self.openai_client.chat.completions.create(
                model=self.openai_deployment,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            return f"I'm sorry, but I encountered an error while generating a response: {str(e)}"
    
    def process_query(self, query: str) -> Dict[str, str]:
        """Process a query using RAG pipeline"""
        logger.info(f"Processing query: {query}")
        
        # Step 1: Retrieve relevant documents
        documents = self.search_documents(query)
        context = "\n\n".join([doc["content"] for doc in documents])
        
        # Step 2: Generate response using retrieved context
        response = self.generate_response(query, context)
        
        return {
            "query": query,
            "response": response,
            "context_used": context,
            "documents_found": len(documents),
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "source": "fullstack-example-rag"
        }

# Global RAG service instance
rag_service = RAGService()

def build_payload(*, prompt: str) -> Dict[str, str]:
    """Legacy function for backward compatibility"""
    return rag_service.process_query(prompt)
