using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;
using System.Net;
using System.Text.Json;

namespace WorkshopRAG.Functions
{
    public class ChatFunction
    {
        private readonly ILogger<ChatFunction> _logger;

        public ChatFunction(ILogger<ChatFunction> logger)
        {
            _logger = logger;
        }

        [Function("chat")]
        [SemanticSearchInput(
            Connection = "AZURE_AI_SEARCH_CONNECTION_STRING",
            IndexName = "hackathon-index",
            Query = "{query}",
            TopK = 5)]
        [TextCompletionInput(
            Connection = "AZURE_OPENAI_CONNECTION_STRING",
            DeploymentName = "chat",
            MaxTokens = 500,
            Temperature = 0.7,
            SystemPrompt = "You are a helpful assistant that answers questions based on the provided context. Use the context to provide accurate and relevant answers. If the context doesn't contain enough information to answer the question, say so politely.",
            UserPrompt = "Context: {search_context}\n\nQuestion: {query}\n\nAnswer:")]
        public async Task<HttpResponseData> Run(
            [HttpTrigger(AuthorizationLevel.Anonymous, "post", Route = "chat")] HttpRequestData req,
            string searchContext,
            string completion)
        {
            _logger.LogInformation("Processing chat request");

            try
            {
                // Parse the request body
                var requestBody = await new StreamReader(req.Body).ReadToEndAsync();
                var requestData = JsonSerializer.Deserialize<ChatRequest>(requestBody);

                if (requestData == null || string.IsNullOrEmpty(requestData.Query))
                {
                    var errorResponse = req.CreateResponse(HttpStatusCode.BadRequest);
                    await errorResponse.WriteStringAsync(JsonSerializer.Serialize(new { error = "Missing 'query' in request body" }));
                    return errorResponse;
                }

                _logger.LogInformation($"Processing query: {requestData.Query}");

                // The bindings automatically handle:
                // 1. Searching Azure AI Search for relevant documents (searchContext)
                // 2. Generating a response using Azure OpenAI with the context (completion)

                var responseData = new
                {
                    query = requestData.Query,
                    response = completion,
                    context_used = searchContext,
                    timestamp = DateTime.UtcNow.ToString("yyyy-MM-ddTHH:mm:ss.fffZ")
                };

                var response = req.CreateResponse(HttpStatusCode.OK);
                response.Headers.Add("Content-Type", "application/json");
                await response.WriteStringAsync(JsonSerializer.Serialize(responseData, new JsonSerializerOptions { WriteIndented = true }));

                return response;
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error processing chat request");
                
                var errorResponse = req.CreateResponse(HttpStatusCode.InternalServerError);
                await errorResponse.WriteStringAsync(JsonSerializer.Serialize(new { error = $"Internal server error: {ex.Message}" }));
                return errorResponse;
            }
        }
    }

    public class ChatRequest
    {
        public string Query { get; set; } = string.Empty;
    }
}
