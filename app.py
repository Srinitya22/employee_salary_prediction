import streamlit as st
import random
import PyPDF2
from babel.numbers import format_currency
import time
from streamlit_lottie import st_lottie
import json
import requests

# 🎨 Page Setup
st.set_page_config(page_title="AI Powered Salary Predictor 💼🇮🇳", page_icon="💰", layout="centered")

# 🌈 Gradient Background Styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #d0f0f0, #ffe5b4, #ffccd5);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        font-family: 'Segoe UI', sans-serif;
    }
    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
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

# Load Lottie animation
@st.cache_data
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

confetti_lottie = load_lottie_url("https://lottie.host/2cfa10a4-8c5d-4706-9771-10e83994f0d2/RddHZvnHYv.json")

# 🎯 Title
st.title("AI Powered Employee Salary Predictor with ATS Score")
st.subheader("Predict salary in ₹ & check your resume score 🔍")

# 📥 Name Input
name = st.text_input("👤 Employee Name")

# 📈 Work Experience
total_exp = st.number_input("🧳 Total Experience (Years)", min_value=0, max_value=40, value=1)

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

# 📄 Resume Upload
uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
resume_text = ""

if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""
    except Exception as e:
        st.error(f"Failed to read PDF: {e}")

# 🔘 Predict Button
if st.button("🔮 Predict Salary & Score"):
    # Dummy logic
    base_salary = 300000
    salary = base_salary + (total_exp * 50000) + (hours_per_week * 1000)

    if marital_status == "Married":
        salary += 20000
    if location in ["Bangalore", "Mumbai", "Delhi"]:
        salary += 50000

    # ATS Score
    ats_keywords = ["python", "sql", "machine learning", "communication", "teamwork", "data analysis"]
    resume_lower = resume_text.lower()
    score = sum(1 for kw in ats_keywords if kw in resume_lower)
    ats_score = int((score / len(ats_keywords)) * 100)

    # Indian style salary
    formatted_salary = format_currency(salary, "INR", locale="en_IN")

    # Output
    st.success(f"💼 Predicted Annual Salary for {name or 'Employee'}: {formatted_salary}")
    st.info(f"📊 ATS Resume Score: {ats_score}%")

    if ats_score < 50:
        st.warning("⚠️ Consider improving your resume with more relevant skills!")
    else:
        st.success("🎉 Awesome! Your resume is well-optimized. Great job!")
        st_lottie(confetti_lottie, height=250, key="confetti")
