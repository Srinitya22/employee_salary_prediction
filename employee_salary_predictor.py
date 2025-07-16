# app.py
import streamlit as st
import random
from PyPDF2 import PdfReader
from docx import Document
import os

st.set_page_config(page_title="Employee Salary Predictor", layout="centered")

# --- Helper functions ---
def extract_text_from_resume(file):
    try:
        if file.name.endswith(".pdf"):
            pdf = PdfReader(file)
            return " ".join(page.extract_text() or '' for page in pdf.pages)
        elif file.name.endswith(".docx"):
            doc = Document(file)
            return " ".join([para.text for para in doc.paragraphs])
    except:
        return ""
    return ""

def calculate_ats_score(resume_text, applied_position):
    resume_words = resume_text.lower().split()
    applied_keywords = applied_position.lower().split()

    if not resume_words:
        return 0

    matched = sum(1 for word in applied_keywords if word in resume_words)
    score = int((matched / len(applied_keywords)) * 100)
    return min(score + random.randint(0, 20), 100)

# --- UI ---
st.title("📊 Employee Salary Predictor")
st.markdown("Upload your resume and fill in the details to predict your salary and ATS score.")

with st.form("prediction_form"):
    resume_file = st.file_uploader("📄 Upload Resume (.pdf or .docx)", type=["pdf", "docx"], required=True)
    name = st.text_input("Full Name")
    gender = st.selectbox("Gender", ["Select", "Male", "Female", "Other"])
    age = st.slider("Age", 18, 65, 25)
    years_exp = st.slider("Years of Experience", 0, 40, 1)
    work_exp = st.slider("Previous Work Experience (Years)", 0, 40, 0)
    marital_status = st.selectbox("Marital Status", ["Select", "Single", "Married"])
    hours_per_week = st.slider("Working Hours Per Week", 20, 80, 40)
    occupation = st.selectbox("Occupation", ["Select", "Software Engineer", "Data Scientist", "Product Manager", "HR Executive", "Marketing Analyst"])
    applied_position = st.selectbox("Applied Position", ["Select", "Junior Developer", "Senior Developer", "Team Lead", "Manager", "Intern"])
    location = st.selectbox("Location", ["Select", "San Francisco", "New York", "Austin", "Seattle", "Remote"])
    
    submitted = st.form_submit_button("🚀 Predict")

if submitted:
    if resume_file is not None and applied_position != "Select":
        resume_text = extract_text_from_resume(resume_file)

        # Salary prediction logic
        base = 30000
        experience_factor = years_exp * 1200
        work_exp_factor = work_exp * 800
        hours_factor = hours_per_week * 60
        place_factor = 10000 if location == 'San Francisco' else 5000 if location == 'New York' else 2000

        salary = base + experience_factor + work_exp_factor + hours_factor + place_factor
        ats_score = calculate_ats_score(resume_text, applied_position)

        st.success("✅ Prediction Complete!")
        st.metric("💰 Predicted Salary", f"${salary:,.0f}")
        st.metric("📈 ATS Score", f"{ats_score}%")
    else:
        st.error("Please complete all fields and upload a resume.")
