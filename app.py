import streamlit as st # type: ignore
import joblib # type: ignore
import numpy as np # type: ignore

# Load model
model = joblib.load('td_loan_model.pkl')

st.title("💰 TD Bank Loan Approval Predictor")

st.write("Enter applicant details below to check loan eligibility:")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)
loan_amt = st.number_input("Loan Amount", min_value=0)
loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 240])
credit = st.selectbox("Credit History (1=Good, 0=Bad)", [1, 0])

if st.button("Predict"):
    sample = np.array([[1 if gender=="Male" else 0,
                        1 if married=="Yes" else 0,
                        0, 0, 0,
                        income, co_income,
                        loan_amt, loan_term,
                        credit, 0, 0, 1]])
    result = model.predict(sample)[0]
    st.success("Loan Approved" if result==1 else "Loan Rejected")
