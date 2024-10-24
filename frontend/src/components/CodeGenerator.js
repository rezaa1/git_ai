import React, { useState } from 'react';
import axios from 'axios';

function CodeGenerator() {
  const [prompt, setPrompt] = useState('');
  const [generatedCode, setGeneratedCode] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/generate-code', { prompt });
      setGeneratedCode(response.data.generated_code);
    } catch (error) {
      console.error('Error generating code:', error);
    }
  };

  return (
    <div>
      <h2>Code Generator</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your code prompt"
        />
        <button type="submit">Generate Code</button>
      </form>
      {generatedCode && (
        <pre>
          <code>{generatedCode}</code>
        </pre>
      )}
    </div>
  );
}

export default CodeGenerator;
