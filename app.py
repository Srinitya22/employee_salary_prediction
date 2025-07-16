import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# 🎨 Background Styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(to right, #ffecd2 0%, #fcb69f 100%);
        color: #000000;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌟 Title
st.title("👩‍💼 Employee Salary Predictor - India 🇮🇳")

# 📍 Sample Indian Locations
locations = [
    "Bengaluru", "Hyderabad", "Mumbai", "Delhi", "Chennai", "Kolkata",
    "Pune", "Ahmedabad", "Jaipur", "Lucknow", "Guwahati", "Bhopal"
]

# 📊 Inputs from user
experience = st.slider("Years of Experience", 0, 30, 2)
location = st.selectbox("Location", locations)
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
industry = st.selectbox("Industry", ["IT", "Finance", "Healthcare", "Education", "Manufacturing"])

# 🔧 Dummy Encoding
def encode_inputs(exp, location, education, industry):
    # For simplicity, encode as numbers
    loc_encoded = locations.index(location)
    edu_map = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
    ind_map = {"IT": 0, "Finance": 1, "Healthcare": 2, "Education": 3, "Manufacturing": 4}
    return [exp, loc_encoded, edu_map[education], ind_map[industry]]

# 🧠 Dummy Training Data (for demo)
np.random.seed(42)
X_train = np.random.randint(0, 20, size=(100, 4))
y_train = X_train[:, 0] * 50000 + np.random.randint(20000, 100000, size=100)  # salary in INR

model = LinearRegression()
model.fit(X_train, y_train)

# 📈 Prediction
if st.button("Predict Salary"):
    features = encode_inputs(experience, location, education, industry)
    prediction = model.predict([features])[0]
    st.success(f"Estimated Salary: ₹{int(prediction):,} /year")
