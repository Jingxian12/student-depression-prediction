import streamlit as st
import joblib
import pandas as pd


# Title
st.title("Student Depression Prediction")

# User inputs
age = st.number_input("Age")
academic_pressure = st.slider("Academic Pressure", 0, 5)

# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "academic_pressure": [academic_pressure]
    })
