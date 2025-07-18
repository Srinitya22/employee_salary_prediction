import streamlit as st
import PyPDF2
from babel.numbers import format_currency

# Streamlit Page Config
st.set_page_config(page_title="AI Salary Predictor 💼", page_icon="💰", layout="centered")

# Custom CSS for pastel background and black text
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom right, #f9e4e4, #e0f7f4, #fdeacc);
    }
    h1, h2, h3, h4, h5, h6 {
        color: black !important;
        font-weight: bold !important;
    }
    label, .stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label {
        color: black !important;
        font-weight: 600;
    }
    .stTextInput input, .stNumberInput input, .stSelectbox div, .stSelectbox input {
        color: black !important;
    }
    .stMarkdown {
        color: black !important;
    }
    .stButton button {
        background-color: #2ecc71;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("💼 AI Powered Employee Salary Predictor 🇮🇳")
st.subheader("🔍 Predict salary in ₹ & check your resume score")

# User Inputs
name = st.text_input("👤 Employee Name")

experience = st.number_input("📘 Total Experience (Years)", min_value=0, max_value=40, value=0)

marital_status = st.selectbox("💍 Marital Status", ["Single", "Married"])

hours_per_week = st.slider("⏰ Hours per Week", min_value=10, max_value=80, value=40)

occupation = st.selectbox("👨‍💻 Current Occupation", [
    "Software Engineer", "Data Analyst", "Web Developer", "Teacher", "HR Executive"
])

applied_role = st.selectbox("🎯 Applied Role", [
    "Junior Developer", "Senior Developer", "Team Lead", "Manager", "Intern"
])

location = st.selectbox("🌍 Location", [
    "Bangalore", "Hyderabad", "Delhi", "Mumbai", "Chennai", "Kolkata", "Pune", "Remote"
])

uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])

# Extract Resume Text
resume_text = ""
if uploaded_file is not None:
    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            resume_text += page.extract_text() or ""
    except:
        st.error("⚠️ Error reading the PDF file.")

# Predict Button
if st.button("🔍 Predict Salary & Score"):
    if uploaded_file is None:
        st.error("⚠️ Please upload your resume before predicting.")
    else:
        # Salary Estimation Logic
        base_salary = 250000
        salary = base_salary + (experience * 50000) + (hours_per_week * 1000)

        if marital_status == "Married":
            salary += 20000
        if location in ["Bangalore", "Mumbai", "Delhi"]:
            salary += 50000
        elif location == "Remote":
            salary -= 30000
        if experience == 0:
            salary = 200000

        formatted_salary = format_currency(salary, 'INR', locale='en_IN').replace(".00", "")

        # ATS Score Calculation
        keywords = ["python", "sql", "machine learning", "communication", "teamwork", "data analysis"]
        resume_lower = resume_text.lower()
        match_count = sum(1 for kw in keywords if kw in resume_lower)
        ats_score = int((match_count / len(keywords)) * 100)

        # Display Predicted Salary
        st.markdown(f"""
            <div style='background-color:#d4edda; padding:12px; border-radius:8px; color:black; font-weight:bold;'>
                💸 Predicted Annual Salary for {name or "Employee"}: {formatted_salary}
            </div>
        """, unsafe_allow_html=True)

        # Display ATS Score
        st.markdown(f"""
            <div style='background-color:#e2e3f3; padding:12px; border-radius:8px; color:black; font-weight:bold;'>
                📊 ATS Resume Score: {ats_score}%
            </div>
        """, unsafe_allow_html=True)

        # Feedback Based on Score
        if ats_score < 50:
            st.warning("⚠️ Consider improving your resume with more relevant skills.")
        else:
            st.success("✅ Great! Your resume looks well-optimized!")

