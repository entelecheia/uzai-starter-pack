# Azure Deployment Samples

Use these assets to deploy the onboarding RAG demo behind an Azure Function.

## Files

- `function_app/__init__.py` — HTTP-triggered Azure Function that calls the shared prompt bridge helper.
- `function_app/function.json` — binding configuration for the HTTP trigger.
- `function_app/prompt_bridge.py` — helper that packages model responses into JSON for clients.
- `host.json` — basic host configuration for local testing.
- `local.settings.json` — sample local configuration values.
- `requirements.txt` — Python packages needed by the Function App runtime.

## Quickstart

```bash
func start
```

Before running, set the environment variable `OPENAI_DEPLOYMENT` to the name of your Azure OpenAI deployment. The included samples return mock data so you can validate plumbing without real credentials.

## Deployment Notes

- Use the `frontend-template` React app as a companion client when demoing the serverless endpoint.
- Update `local.settings.json` with your storage and API keys when you are ready to connect to Azure resources.
