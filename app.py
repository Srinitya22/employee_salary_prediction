import streamlit as st
from babel.numbers import format_currency
import PyPDF2

# 🎨 Page Config
st.set_page_config(page_title="AI Powered Salary Predictor 💼🇮🇳", page_icon="💰", layout="centered")

# ✅ Custom CSS: Full-page pastel gradient background (teal, peach, baby pink)
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        height: 100%;
        background: linear-gradient(135deg, #d0f0f7, #ffe0d2, #fddde6);
        background-attachment: fixed;
    }

    [data-testid="stHeader"], [data-testid="stToolbar"] {
        background: transparent;
    }

    label, .stTextInput label, .stNumberInput label, .stSelectbox label, .stSlider label {
        color: #333333 !important;
        font-weight: 600;
    }

    .stTextInput input, .stSelectbox div, .stNumberInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Title and subtitle
st.title("AI Powered Employee Salary Predictor 🇮🇳")
st.subheader("Predict salary in ₹ & check your resume score 🔍")

# 📥 Form Inputs
name = st.text_input("👤 Employee Name")
total_exp = st.number_input("🧳 Total Experience (Years)", min_value=0, max_value=40, value=0)
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

# 📄 Resume Upload
uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])
resume_text = ""

if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""
    except Exception as e:
        st.error(f"❌ Failed to read PDF: {e}")

# 🔘 Predict Button
if st.button("🔮 Predict Salary & Score"):
    if uploaded_file is None or not resume_text.strip():
        st.error("⚠️ Please upload your resume to proceed with prediction.")
    else:
        # 🧠 Salary Prediction Logic
        base_salary = 200000 if total_exp == 0 else 300000
        salary = base_salary + (total_exp * 45000) + (hours_per_week * 900)

        if marital_status == "Married":
            salary += 20000

        if location in ["Bangalore", "Mumbai", "Delhi"]:
            salary += 40000
        elif location == "Remote":
            salary -= 30000

        # 📊 ATS Resume Scoring
        ats_keywords = ["python", "sql", "machine learning", "communication", "teamwork", "data analysis"]
        resume_lower = resume_text.lower()
        matched_keywords = sum(1 for kw in ats_keywords if kw in resume_lower)
        ats_score = int((matched_keywords / len(ats_keywords)) * 100)

        # 📢 Output Results
        formatted_salary = format_currency(salary, 'INR', locale='en_IN')
        st.success(f"💼 Predicted Annual Salary for {name or 'Employee'}: {formatted_salary}")
        st.info(f"📊 ATS Resume Score: {ats_score}%")

        if ats_score < 50:
            st.warning("⚠️ Consider improving your resume with more relevant skills.")
        else:
            st.success("✅ Great! Your resume is well-optimized.")
