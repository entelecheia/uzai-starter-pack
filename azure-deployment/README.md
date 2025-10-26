# Azure Deployment Module

Learn how to package your prompt and RAG services for Azure, automate resource provisioning, and integrate CI/CD.

## Contents
- Bicep or ARM templates for infrastructure-as-code
- GitHub Actions or Azure DevOps pipelines for automated deployment
- Azure Function or App Service hosting samples

## Setup
```bash
az login
az account set --subscription <subscription-id>
```

Provision resources defined in the module:
```bash
az deployment group create \
  --resource-group <resource-group> \
  --template-file infra/main.bicep \
  --parameters @infra/parameters.json
```

## Next Steps
Deploy your APIs, then hand off the endpoints to the [frontend module](../frontend/README.md) for integration.
