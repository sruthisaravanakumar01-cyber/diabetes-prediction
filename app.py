import streamlit as st
import pickle
import numpy as np

# Load model
with open('linear_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Diabetes Prediction App")

age = st.number_input("Enter Age")

if st.button("Predict"):

    prediction = model.predict([[age]])

    st.success(f"Prediction: {prediction[0]}")
