// frontend/app/page.tsx

'use client';

import { useState } from 'react';

export default function Home() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages([...messages, userMessage]);
    setInput('');

    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: input }),
    });

    const data = await res.json();
    const botMessage = { role: 'assistant', content: data.reply };
    setMessages((prev) => [...prev, botMessage]);
  };

  return (
    <main className="min-h-screen bg-gray-100 p-10">
      <h1 className="text-3xl font-bold mb-6">🎬 Movie Recommender Chatbot</h1>
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-2xl mx-auto">
        <div className="h-80 overflow-y-scroll border p-4 mb-4 rounded">
          {messages.map((msg, i) => (
            <div key={i} className={`mb-2 ${msg.role === 'user' ? 'text-blue-600' : 'text-green-600'}`}>
              <strong>{msg.role === 'user' ? 'You' : 'Bot'}:</strong> {msg.content}
            </div>
          ))}
        </div>
        <div className="flex gap-2">
          <input
            className="flex-1 border border-gray-300 p-2 rounded"
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask me for movie recommendations..."
          />
          <button onClick={sendMessage} className="bg-blue-500 text-white px-4 py-2 rounded">
            Send
          </button>
        </div>
      </div>
    </main>
  );
}
