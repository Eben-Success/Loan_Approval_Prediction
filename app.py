import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# Load the trained model
with open('loan_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define a function to make predictions
def predict_loan_status(data):
    # Preprocess the data
    le = LabelEncoder()
    data['Gender'] = le.fit_transform(data['Gender'])
    data['Married'] = le.fit_transform(data['Married'])
    data['Dependents'] = le.fit_transform(data['Dependents'])
    data['Education'] = le.fit_transform(data['Education'])
    data['Self_Employed'] = le.fit_transform(data['Self_Employed'])
    data['Property_Area'] = le.fit_transform(data['Property_Area'])
    data['Total_Income'] = data['ApplicantIncome'] + data['CoapplicantIncome']

    # Make a prediction
    prediction = model.predict(data)

    # Return the prediction
    return prediction[0]

# Create the web app
st.title("Loan Status Prediction App")

# Add input fields for the user
gender = st.selectbox("Gender", options=['Male', 'Female'])
married = st.selectbox("Marital Status", options=['Yes', 'No'])
dependents = st.slider("Number of Dependents", min_value=0, max_value=10, step=1)
education = st.selectbox("Education", options=['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed", options=['Yes', 'No'])
applicant_income = st.slider("Applicant Income", min_value=0, max_value=100000, step=1000)
coapplicant_income = st.slider("Coapplicant Income", min_value=0, max_value=100000, step=1000)
loan_amount = st.slider("Loan Amount", min_value=0, max_value=100000, step=1000)
loan_amount_term = st.slider("Loan Amount Term (in months)", min_value=0, max_value=1000, step=10)
credit_history = st.selectbox("Credit History", options=[0, 1])
property_area = st.selectbox("Property Area", options=['Rural', 'Semiurban', 'Urban'])

# Create a dictionary from the inputs
data = {
    'Gender': gender,
    'Married': married,
    'Dependents': dependents,
    'Education': education,
    'Self_Employed': self_employed,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'Property_Area': property_area
}

# Convert the dictionary to a pandas dataframe
df = pd.DataFrame(data, index=[0])

# Make a prediction and display the result
if st.button("Predict"):
    prediction = predict_loan_status(df)
    if prediction == 1:
        st.success("Congratulations! You are eligible for the loan.")
    else:
        st.warning("Sorry, you are not eligible for the loan.")
