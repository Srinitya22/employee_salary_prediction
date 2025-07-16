import streamlit as st

st.set_page_config(page_title="Indian Salary Predictor", layout="centered")

# Custom CSS for background and style
st.markdown(
    """
    <style>
    body {
        background-image: linear-gradient(to right, #fceabb, #f8b500);
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🇮🇳 Indian Employee Salary Predictor")
st.caption("🎉 Estimate your annual salary based on your profile!")

# User Inputs
experience = st.number_input("💼 Years of Total Experience", min_value=0, max_value=50, step=1, value=1)
prev_exp = st.number_input("📑 Previous Work Experience (in years)", min_value=0, max_value=50, step=1, value=0)
marital_status = st.selectbox("⚪ Marital Status", ["Single", "Married"])
hours = st.slider("⏰ Hours per Week", min_value=10, max_value=80, value=40)
current_role = st.selectbox("👨‍💻 Current Occupation", ["Software Engineer", "Data Analyst", "Designer", "Project Manager"])
applied_role = st.selectbox("🧲 Applied Role", ["Junior Developer", "Senior Developer", "Data Scientist", "QA Tester"])
location = st.selectbox("📍 Location", ["Bengaluru", "Hyderabad", "Mumbai", "Chennai", "Delhi", "Pune", "Remote"])

# Simple salary estimation logic (mock logic for illustration)
base_salary = 300000  # Base INR
exp_boost = experience * 50000
hours_boost = (hours - 40) * 1000
location_factor = {
    "Bengaluru": 1.3,
    "Hyderabad": 1.2,
    "Mumbai": 1.35,
    "Chennai": 1.15,
    "Delhi": 1.25,
    "Pune": 1.1,
    "Remote": 1.0
}
role_factor = {
    "Junior Developer": 1.0,
    "Senior Developer": 1.5,
    "Data Scientist": 1.7,
    "QA Tester": 1.2
}

salary = (base_salary + exp_boost + hours_boost) * location_factor[location] * role_factor[applied_role]

if st.button("💰 Predict Salary"):
    st.success(f"Estimated Salary: ₹{int(salary):,} /year")
