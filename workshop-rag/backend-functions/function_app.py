import azure.functions as func
import json
import logging
from azure.functions import HttpRequest, HttpResponse
from azure.functions_openai import SemanticSearchInput, TextCompletionInput

app = func.FunctionApp()

@app.function_name("chat")
@app.route(route="chat", methods=["POST"])
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
    system_prompt="You are a helpful assistant that answers questions based on the provided context. Use the context to provide accurate and relevant answers. If the context doesn't contain enough information to answer the question, say so politely.",
    user_prompt="Context: {search_context}\n\nQuestion: {query}\n\nAnswer:"
)
def chat_function(req: HttpRequest, search_context: str, completion: str) -> HttpResponse:
    """
    Azure Function that implements RAG using OpenAI bindings.
    
    This function uses:
    - SemanticSearchInput: Automatically searches Azure AI Search for relevant documents
    - TextCompletionInput: Generates responses using Azure OpenAI with retrieved context
    """
    try:
        # Parse the request body
        req_body = req.get_json()
        if not req_body or 'query' not in req_body:
            return func.HttpResponse(
                json.dumps({"error": "Missing 'query' in request body"}),
                status_code=400,
                mimetype="application/json"
            )
        
        query = req_body['query']
        logging.info(f"Processing query: {query}")
        
        # The bindings automatically handle:
        # 1. Searching Azure AI Search for relevant documents (search_context)
        # 2. Generating a response using Azure OpenAI with the context (completion)
        
        # Return the generated response
        response_data = {
            "query": query,
            "response": completion,
            "context_used": search_context,
            "timestamp": func.datetime.datetime.utcnow().isoformat() + "Z"
        }
        
        return func.HttpResponse(
            json.dumps(response_data, indent=2),
            status_code=200,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return func.HttpResponse(
            json.dumps({"error": f"Internal server error: {str(e)}"}),
            status_code=500,
            mimetype="application/json"
        )
