import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!question) return;

    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    const data = await response.json();

    setChat([...chat, { user: question, bot: data.answer }]);
    setQuestion("");
  };

  return (
    <div style={{ padding: "20px", maxWidth: "600px", margin: "auto" }}>
      <h2>🤖 AI Data Assistant</h2>

      {chat.map((msg, i) => (
        <div key={i}>
          <p><b>You:</b> {msg.user}</p>
          <p><b>Bot:</b> {msg.bot}</p>
          <hr />
        </div>
      ))}

      <input
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask something..."
        style={{ width: "70%", padding: "10px" }}
      />

      <button onClick={sendMessage} style={{ padding: "10px" }}>
        Send
      </button>
    </div>
  );
}

export default App;