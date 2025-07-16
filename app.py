import streamlit as st
import random
import PyPDF2
from babel.numbers import format_currency

# 🎨 Page Setup
st.set_page_config(page_title="AI Powered Salary Predictor 💼🇮🇳", page_icon="💰", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #f7fff7;
        font-family: 'Segoe UI', sans-serif;
    }
    .stApp {
        background: linear-gradient(120deg, #d0f0f0, #ffe0cc, #ffd6e8);
        color: #333;
    }
    input, textarea, select {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    .stTextInput > div > div > input {
        color: #000000 !important;
    }
    .stSelectbox > div > div > div {
        color: #000000 !important;
    }
    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("AI Powered Employee Salary Predictor 🇮🇳")
st.subheader("Predict salary in ₹ & check your resume score 🔍")

# Input Fields
name = st.text_input("👤 Employee Name")
total_exp = st.number_input("🧳 Total Experience (Years)", min_value=0, max_value=40, value=1)
marital_status = st.selectbox("💍 Marital Status", ["Single", "Married"])
hours_per_week = st.slider("⏱️ Hours per Week", min_value=10, max_value=80, value=40)

occupation = st.selectbox("👨‍💻 Current Occupation", [
    "Software Engineer", "Data Analyst", "Web Developer", "Teacher", "HR Executive"
])

applied_role = st.selectbox("🎯 Applied Role", [
    "Junior Developer", "Senior Developer", "Team Lead", "Manager", "Intern"
])

location = st.selectbox("📍 Location", [
    "Bangalore", "Hyderabad", "Delhi", "Mumbai", "Chennai", "Kolkata", "Pune", "Remote"
])

# Resume Upload
uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
resume_text = ""

# 🔮 Predict Button
if st.button("Predict Salary & Resume Score"):
    if uploaded_file is None:
        st.error("🚫 Please upload your resume in PDF format to proceed!")
    else:
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                resume_text += page.extract_text() or ""
        except Exception as e:
            st.error(f"Failed to read PDF: {e}")
        else:
            base_salary = 300000
            salary = base_salary + (total_exp * 50000) + (hours_per_week * 1000)

            if marital_status == "Married":
                salary += 20000

            if location in ["Bangalore", "Mumbai", "Delhi"]:
                salary += 50000

            ats_keywords = ["python", "sql", "machine learning", "communication", "teamwork", "data analysis"]
            resume_lower = resume_text.lower()
            score = sum(1 for kw in ats_keywords if kw in resume_lower)
            ats_score = int((score / len(ats_keywords)) * 100)

            formatted_salary = format_currency(salary, 'INR', locale='en_IN')

            st.success(f"💼 Predicted Annual Salary for {name or 'Employee'}: {formatted_salary}")
            st.info(f"📊 ATS Resume Score: {ats_score}%")

            if ats_score < 50:
                st.warning("⚠️ Consider improving your resume with more relevant skills!")
            else:
                st.toast("✅ Your resume is well-optimized!", icon="🎯")
