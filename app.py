import streamlit as st
import pickle
import numpy as np

@st.cache_resource
def load_model():
    with open('best_logistic_regression_model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️")

st.markdown("""
<style>
.prediction-box {padding: 2rem; border-radius: 10px; text-align: center; font-size: 1.5rem; font-weight: bold; margin: 2rem 0;}
.healthy {background-color: #d4edda; color: #155724; border: 2px solid #c3e6cb;}
.risk {background-color: #f8d7da; color: #721c24; border: 2px solid #f5c6cb;}
</style>
""", unsafe_allow_html=True)

st.title("❤️ Heart Disease Predictor")

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 20, 100, 50)
    sex = st.selectbox("Sex", ["Female", "Male"])
    cp = st.selectbox("Chest Pain", ["Typical", "Atypical", "Non-anginal", "Asymptomatic"])
    trestbps = st.slider("Blood Pressure", 80, 200, 120)
    chol = st.slider("Cholesterol", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120", ["No", "Yes"])
    restecg = st.selectbox("Resting ECG", ["Normal", "Abnormal", "Hypertrophy"])

with col2:
    thalach = st.slider("Max Heart Rate", 60, 220, 150)
    exang = st.selectbox("Exercise Angina", ["No", "Yes"])
    oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0, 0.1)
    slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])
    ca = st.slider("Major Vessels", 0, 3, 0)
    thal = st.selectbox("Thalassemia", ["Normal", "Fixed", "Reversible"])

if st.button("🔍 Predict", type="primary"):
    input_data = np.array([[
        age, 1 if sex == "Male" else 0, 
        ["Typical", "Atypical", "Non-anginal", "Asymptomatic"].index(cp),
        trestbps, chol, 1 if fbs == "Yes" else 0,
        ["Normal", "Abnormal", "Hypertrophy"].index(restecg),
        thalach, 1 if exang == "Yes" else 0, oldpeak,
        ["Up", "Flat", "Down"].index(slope), ca,
        ["Normal", "Fixed", "Reversible"].index(thal)
    ]])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]
    
    if prediction == 0:
        st.markdown(f'<div class="prediction-box healthy">✅ Low Risk<br>Confidence: {probability[0]:.1%}</div>', unsafe_allow_html=True)
        st.balloons()
    else:
        st.markdown(f'<div class="prediction-box risk">⚠️ High Risk<br>Confidence: {probability[1]:.1%}</div>', unsafe_allow_html=True)

st.markdown("**Disclaimer:** For educational purposes only.")