import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("predictive_model.pkl")

# Title
st.set_page_config(page_title="Predictive Maintenance", layout="centered")
st.title("🔧 Predictive Maintenance Dashboard")
st.write("Predict whether a machine is likely to fail using standardized sensor inputs.")

# User input sliders
tp1 = st.slider("Temperature (TP1_iiot)", -3.0, 3.0, 0.0, step=0.1)
pe1 = st.slider("Pressure (PE1_iiot)", -3.0, 3.0, 0.0, step=0.1)
fm1 = st.slider("Vibration/Flow (FM1_iiot)", -3.0, 3.0, 0.0, step=0.1)

# Predict
if st.button("Predict Failure"):
    input_data = np.array([[tp1, pe1, fm1]])
    result = model.predict(input_data)

    if result[0] == 1:
        st.error("⚠️ ALERT: Machine is likely to FAIL soon!")
    else:
        st.success("✅ Machine is functioning normally.")
