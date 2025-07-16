import streamlit as st
import random

# 🎨 Page Setup
st.set_page_config(page_title="AI Powered Employee Salary Predictor with ATS score 💼🇮🇳", page_icon="💰", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #f7fff7;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🇮🇳 Indian Employee Salary Predictor")
st.subheader("Predict salary in ₹ & check your resume score 🔍")

# 📥 Name Input
name = st.text_input("👤 Employee Name")

# 📈 Experience
total_exp = st.number_input("🧳 Total Experience (Years)", min_value=0, max_value=40, value=1)
prev_exp = st.number_input("🔁 Previous Experience (Years)", min_value=0, max_value=40, value=0)

# 💍 Marital Status
marital_status = st.selectbox("💍 Marital Status", ["Single", "Married"])

# ⏱️ Work Hours
hours_per_week = st.slider("⏱️ Hours per Week", min_value=10, max_value=80, value=40)

# 👨‍💻 Current Occupation
occupation = st.selectbox("👨‍💻 Current Occupation", [
    "Software Engineer", "Data Analyst", "Web Developer", "Teacher", "HR Executive"
])

# 🎯 Applied Role
applied_role = st.selectbox("🎯 Applied Role", [
    "Junior Developer", "Senior Developer", "Team Lead", "Manager", "Intern"
])

# 📍 Indian Location
location = st.selectbox("📍 Location", [
    "Bangalore", "Hyderabad", "Delhi", "Mumbai", "Chennai", "Kolkata", "Pune", "Remote"
])

# 📄 Resume Text
resume_text = st.text_area("📄 Paste Your Resume Content (for ATS Score)", height=200)

# 🔘 Predict Button
if st.button("🔮 Predict Salary & Score"):
    # 🔢 Dummy salary prediction logic
    base_salary = 300000  # base in ₹
    salary = base_salary + (total_exp * 50000) + (hours_per_week * 1000)

    if marital_status == "Married":
        salary += 20000

    if location in ["Bangalore", "Mumbai", "Delhi"]:
        salary += 50000  # high cost cities

    # 🎯 ATS Scoring
    ats_keywords = ["python", "sql", "machine learning", "communication", "teamwork", "data analysis"]
    resume_lower = resume_text.lower()
    score = sum(1 for kw in ats_keywords if kw in resume_lower)
    ats_score = int((score / len(ats_keywords)) * 100)

    # 📢 Output
    st.success(f"💼 Predicted Annual Salary for {name or 'Employee'}: ₹ {salary:,.0f}")
    st.info(f"📊 ATS Resume Score: {ats_score}%")

    if ats_score < 50:
        st.warning("⚠️ Consider improving your resume with more relevant skills!")
    else:
        st.balloons()
