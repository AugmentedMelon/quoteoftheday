import React, { useState } from 'react';
import './App.css';

function App() {
  const [quote, setQuote] = useState("");

  const getQuote = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/quote");
      const data = await response.json();
      setQuote(data.quote);  // Update the state with the fetched quote
    } catch (error) {
      console.error("Error fetching quote:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Quote of the Day</h1>
        <p>{quote || "Click the button to get a quote!"}</p>
        <button onClick={getQuote}>Get Quote</button>
      </header>
    </div>
  );
}

export default App;
