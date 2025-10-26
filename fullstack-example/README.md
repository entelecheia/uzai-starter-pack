# Fullstack Example

Combine the prompt engineering, RAG pipeline, and Azure deployment pieces into a cohesive demo.

## Backend

The FastAPI backend located in `backend/app.py` exposes `/api/chat` and returns a mock payload. Start it locally with:

```bash
uvicorn backend.app:app --reload
```

## Frontend

Reuse the `frontend-template` project or start from scratch inside `frontend/` to create a tailored UX for the onboarding scenario.

## Deployment Checklist

- Containerize the backend using `uvicorn` and deploy to Azure Container Apps.
- Configure the Azure Function proxy to forward `/api/chat` requests to the containerized backend.
- Update the frontend environment variables with the deployed API URL.
