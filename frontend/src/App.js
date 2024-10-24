import React from 'react';
import CodeGenerator from './components/CodeGenerator';
import RepositoryManager from './components/RepositoryManager';
import TeamInfo from './components/TeamInfo';

function App() {
  return (
    <div className="App">
      <h1>AI Team Code Generator</h1>
      <CodeGenerator />
      <RepositoryManager />
      <TeamInfo />
    </div>
  );
}

export default App;
