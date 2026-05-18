import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load("model.pkl")

st.set_page_config(page_title="Student Depression Prediction")

st.title("🎓 Student Depression Prediction App")
st.write("Fill in the details below to predict risk.")

# -------------------------
# INPUT FIELDS
# -------------------------

age = st.number_input("Age", 10, 100, 20)

city = st.text_input("City")

academic_pressure = st.slider("Academic Pressure", 0, 10, 5)
work_pressure = st.slider("Work Pressure", 0, 10, 5)

cgpa = st.number_input("CGPA", 0.0, 10.0, 5.0)

study_satisfaction = st.slider("Study Satisfaction", 0, 10, 5)
job_satisfaction = st.slider("Job Satisfaction", 0, 10, 5)

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

family_history = st.selectbox(
    "Family History of Mental Illness",
    ["Yes", "No"]
)

# -------------------------
# PREDICTION
# -------------------------

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [age],
        "City": [city],
        "Academic Pressure": [academic_pressure],
        "Work Pressure": [work_pressure],
        "CGPA": [cgpa],
        "Study Satisfaction": [study_satisfaction],
        "Job Satisfaction": [job_satisfaction],
        "Sleep Duration": [sleep_duration],
        "Dietary Habits": [dietary_habits],
        "Degree": [degree],
        "Have you ever had suicidal thoughts ?": [suicidal_thoughts],
        "Work/Study Hours": [work_study_hours],
        "Financial Stress": [financial_stress],
        "Family History of Mental Illness": [family_history],
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Result")

    if prediction == 1:
        st.error("High risk of depression ⚠️")
    else:
        st.success("Low risk of depression ✅")
