# Azure Deployment

This module contains Azure deployment samples and guides for hosting RAG applications on Azure. It includes both basic Azure Functions samples and comprehensive deployment guides.

## 🏗️ What's Included

### Basic Azure Functions Sample
- `function_app/` — Simple HTTP-triggered Azure Function with mock responses
- `host.json` — Function app configuration
- `local.settings.json` — Local development settings
- `requirements.txt` — Python dependencies

### Workshop Integration
This module works alongside the [Workshop RAG](../workshop-rag/) implementation to provide deployment guidance and samples.

## 🚀 Quick Start

### Prerequisites

1. Complete [Guide 01: Azure Account & Resource Setup](../README.md#guide-01-azure-account--resource-setup)
2. Install Azure Functions Core Tools:
   ```bash
   npm install -g azure-functions-core-tools@4
   ```

### Running the Sample

1. **Navigate to the function app directory:**
   ```bash
   cd azure-deployment
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   ```bash
   cp local.settings.json.example local.settings.json
   # Edit local.settings.json with your values
   ```

4. **Start the function locally:**
   ```bash
   func start
   ```

The function will be available at `http://localhost:7071/api/rag`.

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_DEPLOYMENT` | Name of your Azure OpenAI deployment | Yes |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint URL | Yes |
| `AZURE_OPENAI_KEY` | Azure OpenAI API key | Yes |

### Local Development

The sample function returns mock data by default, so you can test the plumbing without real Azure credentials. To use real Azure services:

1. Update `local.settings.json` with your Azure keys
2. Modify `function_app/prompt_bridge.py` to call actual Azure OpenAI services

## 📚 Deployment Guides

### Azure Functions Deployment

1. **Create a Function App in Azure:**
   ```bash
   az functionapp create \
     --resource-group myResourceGroup \
     --consumption-plan-location westeurope \
     --runtime python \
     --runtime-version 3.10 \
     --functions-version 4 \
     --name myFunctionApp \
     --storage-account mystorageaccount
   ```

2. **Deploy the function:**
   ```bash
   func azure functionapp publish myFunctionApp
   ```

3. **Configure application settings:**
   ```bash
   az functionapp config appsettings set \
     --name myFunctionApp \
     --resource-group myResourceGroup \
     --settings OPENAI_DEPLOYMENT=chat
   ```

### Azure Static Web Apps Deployment

For complete RAG applications, use the [Workshop RAG](../workshop-rag/) implementation with Azure Static Web Apps:

1. **Deploy the frontend and backend together:**
   ```bash
   swa deploy
   ```

2. **Configure environment variables in Azure:**
   - Go to your Static Web App in the Azure Portal
   - Navigate to Configuration
   - Add your Azure OpenAI and AI Search connection strings

## 🔗 Integration with Other Modules

### Workshop RAG
The [Workshop RAG](../workshop-rag/) module provides a complete implementation using Azure Functions with OpenAI bindings. This deployment module provides the foundation for deploying such applications.

### Fullstack Example
The [Fullstack Example](../fullstack-example/) uses FastAPI and can be deployed using Azure Container Apps or Azure App Service.

## 🛠️ Advanced Configuration

### Custom Domains
Configure custom domains for your Azure Functions:

```bash
az functionapp config hostname add \
  --hostname api.mycompany.com \
  --name myFunctionApp \
  --resource-group myResourceGroup
```

### Authentication
Add authentication to your Azure Functions:

1. Enable App Service Authentication in the Azure Portal
2. Configure identity providers (Azure AD, Google, etc.)
3. Update your function code to validate tokens

### Monitoring
Set up monitoring and logging:

1. Enable Application Insights
2. Configure custom metrics
3. Set up alerts for errors and performance issues

## 🐛 Troubleshooting

### Common Issues

1. **Function Not Starting**: Check your `local.settings.json` configuration
2. **CORS Errors**: Ensure CORS is properly configured in `host.json`
3. **Authentication Errors**: Verify your Azure OpenAI keys and endpoints
4. **Deployment Failures**: Check your Azure CLI login and permissions

### Debug Mode

Enable detailed logging:

```bash
func start --verbose
```

## 📚 Next Steps

1. **Explore Workshop RAG**: Use the complete implementation in the [Workshop RAG](../workshop-rag/) module
2. **Add Monitoring**: Implement Application Insights for production monitoring
3. **Scale Up**: Configure auto-scaling for high-traffic scenarios
4. **Security**: Implement authentication and authorization

## 🔗 Related Resources

- [Azure Functions Documentation](https://learn.microsoft.com/azure/azure-functions/)
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/)
- [Azure CLI Documentation](https://learn.microsoft.com/cli/azure/)
- [Workshop Guide](../README.md#getting-started-onboarding-guides)
