import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('data/sales_data.pkl')

# Streamlit app title
st.title(" Sales Revenue Prediction")
st.markdown("Enter sales details below to predict revenue.")

# Input fields
qty = st.number_input("Quantity Ordered", min_value=1, max_value=1000, value=50)
price = st.number_input("Price Each", min_value=1.0, max_value=1000.0, value=99.99)
month = st.selectbox("Month", list(range(1, 13)))
year = st.selectbox("Year", [2003, 2004, 2005])

# Predict button
if st.button("🔮 Predict Revenue"):
    input_data = np.array([[qty, price, month, year]])
    predicted_revenue = model.predict(input_data)
    st.success(f" Predicted Revenue: ₹ {round(predicted_revenue[0], 2)}")