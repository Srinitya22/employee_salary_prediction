import streamlit as st
import PyPDF2
from babel.numbers import format_currency

# Page Setup
st.set_page_config(page_title="AI Powered Salary Predictor 💼🇮🇳", page_icon="💰", layout="centered")

# Custom CSS for pastel background and dark text
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to bottom right, #f9e4e4, #e0f7f4, #fdeacc);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #000000 !important;
        font-weight: bold !important;
    }
    label, .stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label {
        color: #000000 !important;
        font-weight: 500;
    }
    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title & Subtitle
st.title("💼 AI Powered Employee Salary Predictor 🇮🇳")
st.subheader("🔍 Predict salary in ₹ & check your resume score")

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

if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""
    except Exception as e:
        st.error(f"Failed to read PDF: {e}")

# Predict Button
if st.button("🔍 Predict Salary & Score"):
    if uploaded_file is None:
        st.error("⚠️ Please upload your resume before predicting.")
    else:
        # Dummy salary prediction logic
        base_salary = 250000  # fresher base
        salary = base_salary + (total_exp * 50000) + (hours_per_week * 1000)

        if marital_status == "Married":
            salary += 20000

        if location in ["Bangalore", "Mumbai", "Delhi"]:
            salary += 50000  # metro cities

        if location == "Remote":
            salary -= 30000  # less compensation for remote

        if total_exp == 0:
            salary = 200000  # default for freshers

        # Format salary in Indian notation
        formatted_salary = format_currency(salary, 'INR', locale='en_IN').replace(".00", "")

        # ATS Scoring
        ats_keywords = ["python", "sql", "machine learning", "communication", "teamwork", "data analysis"]
        resume_lower = resume_text.lower()
        score = sum(1 for kw in ats_keywords if kw in resume_lower)
        ats_score = int((score / len(ats_keywords)) * 100)

        # Output Display
        st.markdown(f"""
            <div style='background-color:#d4edda; padding:12px; border-radius:8px; color:black; font-weight:bold;'>
                💼 Predicted Annual Salary for {name or 'Employee'}: {formatted_salary}
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div style='background-color:#d1ecf1; padding:12px; border-radius:8px; color:black; font-weight:bold;'>
                📊 ATS Resume Score: {ats_score}%
            </div>
        """, unsafe_allow_html=True)

        if ats_score < 50:
            st.warning("⚠️ Consider improving your resume with more relevant skills!")
        else:
            st.success("✅ Great! Your resume looks well-optimized!")
            
