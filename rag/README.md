# Retrieval-Augmented Generation (RAG) Module

This module provides foundational knowledge and tools for building RAG (Retrieval-Augmented Generation) systems. Learn how to ground your prompts with domain knowledge using Azure AI Search and vector databases.

## 🎯 What You'll Learn

- **RAG Architecture**: Understand how retrieval and generation work together
- **Document Processing**: Learn to ingest and index various document types
- **Vector Search**: Implement semantic search using Azure AI Search
- **Response Generation**: Combine retrieved context with AI-generated responses
- **Best Practices**: Follow industry standards for RAG implementation

## 🏗️ RAG Architecture Overview

RAG (Retrieval-Augmented Generation) is a technique that combines information retrieval with text generation to create more accurate and contextually relevant AI responses.

### How RAG Works

1. **Document Ingestion**: Process and index your documents in a searchable format
2. **Query Processing**: When a user asks a question, convert it to a search query
3. **Retrieval**: Search your document index for relevant information
4. **Augmentation**: Combine the retrieved context with the user's question
5. **Generation**: Use an AI model to generate a response based on the augmented prompt

### Benefits of RAG

- **Up-to-date Information**: Access current data beyond the AI model's training cutoff
- **Domain Expertise**: Ground responses in your specific knowledge base
- **Transparency**: Show users the sources used for responses
- **Cost Efficiency**: Reduce hallucination and improve response quality

## 📁 Module Contents

- **Data Ingestion**: Scripts and notebooks for processing various document types
- **Indexing Utilities**: Tools for creating and managing search indexes
- **API Services**: Complete RAG pipeline implementations
- **Examples**: Sample implementations for different use cases

## 🚀 Quick Start

### Prerequisites

1. Complete [Guide 01: Azure Account & Resource Setup](../README.md#guide-01-azure-account--resource-setup)
2. Python 3.10+ installed
3. Azure AI Search service provisioned
4. Azure OpenAI service provisioned

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   ```bash
   export OPENAI_API_KEY="sk-your-openai-key"
   export AZURE_OPENAI_ENDPOINT="https://<your-resource-name>.openai.azure.com/"
   export AZURE_OPENAI_KEY="your-azure-openai-key"
   export AZURE_SEARCH_ENDPOINT="https://<your-search-resource>.search.windows.net/"
   export AZURE_SEARCH_KEY="your-azure-search-key"
   ```

3. **Run the ingestion pipeline:**
   ```bash
   python ingest.py
   ```

4. **Start the RAG service:**
   ```bash
   python app.py
   ```

## 🔧 Implementation Examples

### Basic RAG Pipeline

```python
from azure.search.documents import SearchClient
from openai import AzureOpenAI

def rag_pipeline(query: str):
    # 1. Search for relevant documents
    search_client = SearchClient(endpoint, index_name, credential)
    results = search_client.search(search_text=query, top=5)
    
    # 2. Extract context
    context = "\n".join([doc["content"] for doc in results])
    
    # 3. Generate response
    openai_client = AzureOpenAI(endpoint=openai_endpoint, api_key=openai_key)
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Answer based on the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
    )
    
    return response.choices[0].message.content
```

### Advanced RAG with Vector Search

```python
def vector_rag_pipeline(query: str):
    # 1. Generate query embedding
    query_embedding = openai_client.embeddings.create(
        model="text-embedding-ada-002",
        input=query
    ).data[0].embedding
    
    # 2. Vector search
    results = search_client.search(
        search_text="",
        vector_queries=[{
            "vector": query_embedding,
            "k_nearest_neighbors": 5,
            "fields": "content_vector"
        }]
    )
    
    # 3. Generate response with retrieved context
    # ... (similar to basic RAG)
```

## 🛠️ Configuration Options

### Search Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `top_k` | Number of documents to retrieve | 5 |
| `search_mode` | Search mode (simple, full) | full |
| `query_type` | Query type (simple, full, semantic) | semantic |
| `scoring_profile` | Custom scoring profile | None |

### AI Model Settings

| Parameter | Description | Default |
|-----------|-------------|---------|
| `model` | OpenAI model to use | gpt-4 |
| `max_tokens` | Maximum response length | 500 |
| `temperature` | Response creativity (0-1) | 0.7 |
| `system_prompt` | System message for the AI | Custom RAG prompt |

## 🔗 Integration with Other Modules

### Workshop RAG
The [Workshop RAG](../workshop-rag/) module provides a complete, ready-to-run implementation using Azure Functions with OpenAI bindings.

### Fullstack Example
The [Fullstack Example](../fullstack-example/) shows how to integrate RAG into a FastAPI application with full control over the pipeline.

### Prompt Engineering
The [Prompt Engineering](../prompt-engineering/) module teaches you how to craft effective prompts for RAG systems.

## 📚 Best Practices

### Document Processing
- **Chunk Size**: Use 512-1024 tokens per chunk for optimal retrieval
- **Overlap**: Include 10-20% overlap between chunks to maintain context
- **Metadata**: Include relevant metadata (title, source, date) for filtering

### Search Optimization
- **Index Design**: Create indexes optimized for your content type
- **Scoring Profiles**: Use custom scoring profiles for domain-specific ranking
- **Filters**: Implement filters for document type, date range, etc.

### Response Quality
- **Context Length**: Limit context to avoid token limits and maintain relevance
- **Source Attribution**: Include source information in responses
- **Fallback Handling**: Provide graceful fallbacks when no relevant context is found

## 🐛 Troubleshooting

### Common Issues

1. **No Search Results**: Check your index configuration and document ingestion
2. **Poor Response Quality**: Adjust chunk size, search parameters, or prompts
3. **Token Limits**: Reduce context length or implement context summarization
4. **Slow Performance**: Optimize your search index and consider caching

### Debug Mode

Enable detailed logging to troubleshoot issues:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📚 Next Steps

1. **Explore Complete Implementations**: Check out [Workshop RAG](../workshop-rag/) and [Fullstack Example](../fullstack-example/)
2. **Deploy to Azure**: Use the [Azure Deployment](../azure-deployment/) module
3. **Add Advanced Features**: Implement conversation memory, multi-modal search, etc.
4. **Optimize Performance**: Add caching, implement async processing, etc.

## 🔗 Related Resources

- [Azure AI Search Documentation](https://learn.microsoft.com/azure/search/)
- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [RAG Best Practices](https://learn.microsoft.com/azure/ai-services/openai/concepts/rag)
- [Vector Search Guide](https://learn.microsoft.com/azure/search/vector-search-overview)
