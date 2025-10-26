# Frontend Module

Build modern, responsive frontend experiences that consume RAG APIs and showcase AI features. This module provides React-based components and examples for creating engaging user interfaces.

## 🎯 What You'll Learn

- **Modern Frontend Development**: Build responsive UIs with React and TypeScript
- **API Integration**: Connect frontend applications to RAG backends
- **Authentication**: Implement Azure Active Directory authentication
- **User Experience**: Design intuitive interfaces for AI-powered applications
- **State Management**: Handle complex application state and data flow

## 🏗️ Frontend Architecture

### Technology Stack

- **React 18**: Modern React with hooks and concurrent features
- **TypeScript**: Type-safe JavaScript for better development experience
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework for rapid styling
- **Axios**: HTTP client for API communication

### Component Structure

```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Chat/           # Chat interface components
│   │   ├── Document/       # Document exploration components
│   │   └── Auth/           # Authentication components
│   ├── hooks/              # Custom React hooks
│   ├── services/           # API service layer
│   ├── types/              # TypeScript type definitions
│   └── utils/              # Utility functions
├── public/                 # Static assets
└── package.json           # Dependencies and scripts
```

## 🚀 Quick Start

### Prerequisites

1. Node.js 18+ installed
2. A RAG backend running (from [Workshop RAG](../workshop-rag/) or [Fullstack Example](../fullstack-example/))

### Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env.local
   # Edit .env.local with your backend URL
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

The application will be available at `http://localhost:5173`.

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `VITE_API_BASE_URL` | Backend API base URL | Yes |
| `VITE_AZURE_AD_CLIENT_ID` | Azure AD client ID for authentication | No |
| `VITE_APP_TITLE` | Application title | No |

### Example Configuration

```bash
# .env.local
VITE_API_BASE_URL="http://localhost:8000"
VITE_AZURE_AD_CLIENT_ID="your-client-id"
VITE_APP_TITLE="RAG Chat Application"
```

## 🎨 UI Components

### Chat Interface

The chat interface provides a modern, responsive design for conversational AI:

```tsx
import { ChatInterface } from './components/Chat/ChatInterface';

function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      <ChatInterface 
        apiUrl={import.meta.env.VITE_API_BASE_URL}
        onMessage={(message) => console.log('New message:', message)}
      />
    </div>
  );
}
```

### Document Explorer

Browse and search through your document collection:

```tsx
import { DocumentExplorer } from './components/Document/DocumentExplorer';

function App() {
  return (
    <DocumentExplorer
      documents={documents}
      onDocumentSelect={(doc) => console.log('Selected:', doc)}
      searchPlaceholder="Search documents..."
    />
  );
}
```

### Authentication

Integrate Azure Active Directory authentication:

```tsx
import { AuthProvider } from './components/Auth/AuthProvider';
import { LoginButton } from './components/Auth/LoginButton';

function App() {
  return (
    <AuthProvider>
      <div className="app">
        <LoginButton />
        {/* Rest of your app */}
      </div>
    </AuthProvider>
  );
}
```

## 🔗 API Integration

### Chat Service

```typescript
// services/chatService.ts
import axios from 'axios';

export interface ChatMessage {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
}

export interface ChatResponse {
  message: string;
  sources?: string[];
  metadata?: Record<string, any>;
}

export class ChatService {
  private apiUrl: string;

  constructor(apiUrl: string) {
    this.apiUrl = apiUrl;
  }

  async sendMessage(message: string): Promise<ChatResponse> {
    const response = await axios.post(`${this.apiUrl}/api/chat`, {
      message
    });
    return response.data;
  }
}
```

### Document Service

```typescript
// services/documentService.ts
export interface Document {
  id: string;
  title: string;
  content: string;
  source: string;
  metadata: Record<string, any>;
}

export class DocumentService {
  private apiUrl: string;

  constructor(apiUrl: string) {
    this.apiUrl = apiUrl;
  }

  async searchDocuments(query: string): Promise<Document[]> {
    const response = await axios.get(`${this.apiUrl}/api/search`, {
      params: { q: query }
    });
    return response.data.documents;
  }
}
```

## 🎨 Styling and Theming

### Tailwind CSS Configuration

The project uses Tailwind CSS for styling. Customize the theme in `tailwind.config.js`:

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#3b82f6',
          900: '#1e3a8a',
        }
      }
    }
  }
}
```

### Custom Components

Create reusable styled components:

```tsx
// components/ui/Button.tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children,
  onClick
}) => {
  const baseClasses = 'font-medium rounded-lg transition-colors';
  const variantClasses = {
    primary: 'bg-blue-600 text-white hover:bg-blue-700',
    secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
    outline: 'border border-gray-300 text-gray-700 hover:bg-gray-50'
  };
  const sizeClasses = {
    sm: 'px-3 py-1.5 text-sm',
    md: 'px-4 py-2 text-base',
    lg: 'px-6 py-3 text-lg'
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
};
```

## 🔗 Integration with Backends

### Workshop RAG Integration

Connect to the Azure Functions backend:

```typescript
// config/api.ts
export const API_CONFIG = {
  baseUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:7071',
  endpoints: {
    chat: '/api/chat',
    search: '/api/search'
  }
};
```

### Fullstack Example Integration

Connect to the FastAPI backend:

```typescript
// config/api.ts
export const API_CONFIG = {
  baseUrl: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  endpoints: {
    chat: '/api/chat',
    search: '/api/search',
    health: '/health'
  }
};
```

## 🚀 Deployment

### Static Web Apps

Deploy to Azure Static Web Apps:

```bash
# Build the application
npm run build

# Deploy using Azure CLI
az staticwebapp create \
  --name my-rag-app \
  --resource-group myResourceGroup \
  --source . \
  --location "Central US" \
  --branch main
```

### Docker Deployment

Create a Dockerfile for containerized deployment:

```dockerfile
FROM node:18-alpine

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000
CMD ["npm", "run", "preview"]
```

## 🐛 Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure your backend allows requests from your frontend domain
2. **API Connection Issues**: Verify your `VITE_API_BASE_URL` is correct
3. **Build Failures**: Check for TypeScript errors and missing dependencies
4. **Authentication Issues**: Verify your Azure AD configuration

### Debug Mode

Enable debug logging:

```typescript
// utils/logger.ts
export const logger = {
  debug: (message: string, data?: any) => {
    if (import.meta.env.DEV) {
      console.log(`[DEBUG] ${message}`, data);
    }
  }
};
```

## 📚 Next Steps

1. **Explore Complete Examples**: Check out [Workshop RAG](../workshop-rag/) and [Fullstack Example](../fullstack-example/) for complete implementations
2. **Add Advanced Features**: Implement real-time updates, file uploads, etc.
3. **Optimize Performance**: Add lazy loading, code splitting, etc.
4. **Deploy to Production**: Use Azure Static Web Apps or other hosting platforms

## 🔗 Related Resources

- [React Documentation](https://react.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [Vite Documentation](https://vitejs.dev/)
- [Azure Static Web Apps Documentation](https://learn.microsoft.com/azure/static-web-apps/)
