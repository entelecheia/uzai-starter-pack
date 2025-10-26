import { useState } from 'react';
import axios from 'axios';

const DEFAULT_MESSAGE = 'Summarize the latest onboarding tutorial.';

export function App() {
  const [message, setMessage] = useState(DEFAULT_MESSAGE);
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    try {
      const { data } = await axios.post('/api/rag', { message });
      setResponse(JSON.stringify(data, null, 2));
    } catch (error) {
      setResponse(`Error: ${error.message}`);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="container">
      <h1>Onboarding Frontend Template</h1>
      <p>Connect this UI to the Azure Function defined in <code>azure-deployment/</code>.</p>

      <form onSubmit={handleSubmit}>
        <label htmlFor="message">User message</label>
        <textarea
          id="message"
          value={message}
          onChange={(event) => setMessage(event.target.value)}
          rows={4}
        />
        <button type="submit" disabled={isLoading}>
          {isLoading ? 'Sending...' : 'Send to API'}
        </button>
      </form>

      <section className="response">
        <h2>API Response</h2>
        <pre>{response}</pre>
      </section>
    </main>
  );
}

export default App;
