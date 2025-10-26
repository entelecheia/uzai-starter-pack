# Frontend Template

This Vite + React starter provides a minimal client for interacting with the onboarding APIs.

## Scripts

- `npm install` — install dependencies.
- `npm run dev` — start the local development server.
- `npm run build` — create a production build.

## Integration Notes

Update the Axios call in `src/App.jsx` with the deployed Azure Function URL once the backend is live. The default `/api/rag` path assumes a local proxy pointing to the serverless endpoint.
