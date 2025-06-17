import React from 'react';
import Header from './components/Header';
import Insights from './components/Insights';
import Charts from './components/Charts';

function App() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <div className="container mx-auto p-4">
        <Insights />
        <Charts />
      </div>
    </div>
  );
}

export default App;