import React, { useState, useEffect } from 'react';

function Insights() {
  const [insights, setInsights] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/insights')
      .then(response => response.json())
      .then(data => setInsights(data))
      .catch(err => setError(err.message));
  }, []);

  if (error) return <div className="text-red-500">Error: {error}</div>;
  if (!insights) return <div>Loading...</div>;

  return (
    <div className="mb-8">
      <h2 className="text-xl font-semibold mb-4">Key Insights</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-white p-4 rounded shadow">
          <p className="text-lg">Average Purchase Amount</p>
          <p className="text-2xl font-bold">${insights.avg_purchase}</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <p className="text-lg">Top Category</p>
          <p className="text-2xl font-bold">{insights.top_category}</p>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <p className="text-lg">Promo Code Usage</p>
          <p className="text-2xl font-bold">{insights.promo_usage}%</p>
        </div>
      </div>
    </div>
  );
}

export default Insights;