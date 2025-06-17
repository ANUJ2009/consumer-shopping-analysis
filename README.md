Consumer Shopping Analysis
A web application to analyze and visualize the Consumer Behavior and Shopping Habits Dataset.
Setup
Backend

Navigate to backend:cd backend


Create a virtual environment and activate it:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:pip install -r requirements.txt


Download shopping_behavior_updated.csv from Kaggle and place it in backend/data/.
Run the Flask app:python app.py



Frontend

Navigate to frontend:cd frontend


Install dependencies:npm install


Start the React app:npm start



Usage

Access the app at http://localhost:3000.
The backend API runs at http://localhost:5000.

Dataset

Source: Kaggle Consumer Behavior and Shopping Habits Dataset.
File: backend/data/shopping_behavior_updated.csv.

