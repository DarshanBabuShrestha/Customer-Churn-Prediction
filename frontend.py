import streamlit as st
import requests

st.title("Customer Churn Prediction Frontend")

st.write("Enter customer details to predict churn:")

gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
streaming_tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
streaming_movies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

# Prepare input for backend (update keys as per your model)
data = {
    'gender': 1 if gender == "Male" else 0,
    'SeniorCitizen': senior_citizen,
    'Partner': 1 if partner == "Yes" else 0,
    'Dependents': 1 if dependents == "Yes" else 0,
    'tenure': tenure,
    'PhoneService': 1 if phone_service == "Yes" else 0,
    'MultipleLines': ["No phone service", "No", "Yes"].index(multiple_lines),
    'InternetService': ["DSL", "Fiber optic", "No"].index(internet_service),
    'OnlineSecurity': ["No internet service", "No", "Yes"].index(online_security),
    'OnlineBackup': ["No internet service", "No", "Yes"].index(online_backup),
    'DeviceProtection': ["No internet service", "No", "Yes"].index(device_protection),
    'TechSupport': ["No internet service", "No", "Yes"].index(tech_support),
    'StreamingTV': ["No internet service", "No", "Yes"].index(streaming_tv),
    'StreamingMovies': ["No internet service", "No", "Yes"].index(streaming_movies),
    'Contract': ["Month-to-month", "One year", "Two year"].index(contract),
    'PaperlessBilling': 1 if paperless_billing == "Yes" else 0,
    'PaymentMethod': ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"].index(payment_method),
    'MonthlyCharges': monthly_charges,
    'TotalCharges': total_charges
}

if st.button("Predict Churn"):
    response = requests.post("http://127.0.0.1:5000/predict", json=data)
    if response.status_code == 200:
        result = response.json()['churn_prediction']
        st.success(f"Churn Prediction: {'Yes' if result == 1 else 'No'}")
    else:
        st.error("Error: Could not get prediction from backend.")
