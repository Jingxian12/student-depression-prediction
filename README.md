# student-depression-prediction
An end-to-end machine learning project for early student depression risk prediction with XGBoost, threshold tuning, and Streamlit deployment.

## 1. Overview
This project is a machine learning-based web application that predicts the likelihood of depression risk among students based on lifestyle, academic, and personal factors.

**The application is built using:**
- Python
- Scikit-learn
- Streamlit

The goal of this project is to provide an early screening tool for awareness and educational purposes.

## 2. Dataset
The dataset used in this project was obtained from Kaggle:

- Student Depression Dataset by Shodolamu Opeyemi
- Source: [https://www.kaggle.com/...](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)

The dataset contains student-related information such as:
- Age
- Academic pressure
- CGPA
- Sleep duration
- Dietary habits
- Financial stress
- Work/study hours
- Suicidal thoughts
- Family history of mental illness
- Degree and city information


## 3. Data Preprocessing
Several preprocessing techniques were applied:
- Missing value imputation
- Feature scaling
- One-hot encoding
- Ordinal encoding
- Binary encoding

## 4. Machine Learning Pipeline
The project uses a Scikit-learn `Pipeline` and `ColumnTransformer` for preprocessing and model training.

### Numerical Features
- Median imputation
- Standard scaling

### Categorical Features
- One-hot encoding with unknown category handling

### Ordinal Features
Custom ordinal encoding for:
- Sleep duration
- Dietary habits

### Binary Features
Ordinal encoding for binary yes/no variables.

The trained model was exported using `joblib`.

## 5. Model Performance

The prediction threshold was adjusted to improve recall and reduce false negatives.

This means the model prioritizes identifying potentially at-risk students, even if some false positives occur.

This tradeoff is important in mental health screening applications, where missing a high-risk individual may be more harmful than incorrectly flagging a low-risk individual.

Disclaimer

This application is intended for educational and early screening purposes only.

It is NOT a medical diagnosis tool and should not replace professional mental health assessment, diagnosis, or treatment.

If you or someone you know is experiencing mental health difficulties, please seek support from a qualified healthcare professional.

