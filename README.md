# ai4all
portfolio project

# Customer Churn Prediction Project

This project predicts customer churn using machine learning. It includes a backend API, a Streamlit frontend, and a Jupyter notebook for model development.

## Project Structure
- `main.ipynb`: Jupyter notebook for data analysis, model training, and export.
- `backend.py`: Flask API serving the trained model for predictions.
- `frontend.py`: Streamlit app for user input and displaying churn predictions.
- `dataset.csv`: The dataset used for training and evaluation.
- `best_churn_model.pkl`: Exported trained model.

## How to Run

### 1. Setup Python Environment
Create and activate a virtual environment (recommended):
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install required packages:
```sh
pip install -r requirements.txt
# Or install manually:
pip install pandas scikit-learn matplotlib seaborn joblib flask streamlit requests
```

### 2. Train and Export the Model
Open `main.ipynb` and run all cells to:
- Load and preprocess data
- Train models
- Export the best model as `best_churn_model.pkl`

### 3. Start the Backend API
Run the backend server:
```sh
python backend.py
```
This starts a Flask API at `http://127.0.0.1:5000/predict`.

### 4. Start the Frontend
In a new terminal, run:
```sh
streamlit run frontend.py
```
This opens the Streamlit app in your browser for making predictions.

## Usage
- Enter customer details in the Streamlit app.
- Click "Predict Churn" to see the prediction result.

## Requirements
- Python 3.8+
- pandas, scikit-learn, matplotlib, seaborn, joblib, flask, streamlit, requests

## Notes
- Ensure the backend is running before using the frontend.
- You can retrain the model by rerunning the notebook.

## License
MIT License
