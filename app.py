from flask import Flask, jsonify, send_file
from analysis import analyze_data
import os

app = Flask(__name__)

DATA_FILE = 'data/shopping_behavior_updated.csv'

@app.route('/api/insights', methods=['GET'])
def get_insights():
    """Return key insights from the dataset."""
    try:
        insights = analyze_data(DATA_FILE)
        return jsonify(insights)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/plots/<plot_name>', methods=['GET'])
def get_plot(plot_name):
    """Serve plot images."""
    plot_path = os.path.join('static/plots', plot_name)
    if os.path.exists(plot_path):
        return send_file(plot_path, mimetype='image/png')
    return jsonify({'error': 'Plot not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)