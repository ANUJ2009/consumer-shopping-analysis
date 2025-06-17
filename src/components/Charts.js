import React from 'react';

function Charts() {
  const plots = [
    'purchase_by_gender_age.png',
    'top_categories.png',
    'promo_by_location.png',
    'correlation_heatmap.png'
  ];

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Visualizations</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {plots.map(plot => (
          <div key={plot} className="bg-white p-4 rounded shadow">
            <img
              src={`http://localhost:5000/api/plots/${plot}`}
              alt={plot}
              className="w-full h-auto"
            />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Charts;