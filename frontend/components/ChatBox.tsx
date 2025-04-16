// frontend/app/page.tsx or frontend/pages/index.tsx
"use client";
import { useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const handleSend = async () => {
    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await res.json();
    setResponse(data.reply);
  };

  return (
    <main style={{ padding: "2rem" }}>
      <h1>🎬 MovieBot</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask for movie recommendations..."
        style={{ padding: "10px", width: "60%" }}
      />
      <button onClick={handleSend} style={{ marginLeft: "10px" }}>
        Send
      </button>
      <div style={{ marginTop: "20px" }}>
        <strong>Bot:</strong> {response}
      </div>
    </main>
  );
}
