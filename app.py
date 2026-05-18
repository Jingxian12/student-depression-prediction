import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.joblib")

st.set_page_config(page_title="Student Depression Prediction")

st.title("🎓 Student Depression Prediction App")
st.write("Fill in the details below to predict risk.")

# -------------------------
# INPUT FIELDS
# -------------------------

age = st.number_input("Age", 10, 100, 20)
city = st.text_input("City")
academic_pressure = st.slider("Academic Pressure", 0, 10, 5)
cgpa = st.number_input("CGPA", 0.0, 10.0, 5.0)

study_satisfaction = st.slider("Study Satisfaction", 0, 10, 5)
sleep_duration = st.selectbox(
    "Sleep Duration",
    ["<5 hours", "5-6 hours", "6-7 hours", "7-8 hours", ">8 hours"]
)
dietary_habits = st.selectbox(
    "Dietary Habits",
    ["Healthy", "Moderate", "Unhealthy"]
)

degree = st.text_input("Degree")
suicidal_thoughts = st.selectbox(
    "Have you ever had suicidal thoughts?",
    ["Yes", "No"]
)

work_study_hours = st.number_input("Work/Study Hours per day", 0, 24, 5)
financial_stress = st.slider("Financial Stress", 0, 10, 5)

family_history_mental_illness = st.selectbox(
    "Family History of Mental Illness",
    ["Yes", "No"]
)

# -------------------------
# PREDICTION
# -------------------------

if st.button("Predict"):

    input_data = pd.DataFrame({
        "age": [age],
        "city": [city],
        "academic_pressure": [academic_pressure],
        "cgpa": [cgpa],
        "study_satisfaction": [study_satisfaction],
        "sleep_duration": [sleep_duration],
        "dietary_habits": [dietary_habits],
        "degree": [degree],
        "suicidal_thoughts": [suicidal_thoughts],
        "work_study_hours": [work_study_hours],
        "financial_stress": [financial_stress],
        "family_history_mental_illness": [family_history_mental_illness],
    })
    input_data = input_data[model.feature_names_in_]

    proba = model.predict_proba(input_data)[0][1]  # probability of class 1
    threshold = 0.44110572
    prediction = 1 if proba >= threshold else 0

    st.subheader("Result")

    if prediction == 1:
        st.error("High risk of depression ⚠️")
    else:
        st.success("Low risk of depression ✅")
