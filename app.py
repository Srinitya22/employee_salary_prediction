import streamlit as st
import random
from PyPDF2 import PdfReader
from docx import Document
import io

st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="centered")

# Options
occupations = ["Software Engineer", "Data Scientist", "Product Manager", "HR Executive", "Marketing Analyst"]
positions = ["Junior Developer", "Senior Developer", "Team Lead", "Manager", "Intern"]
locations = ["San Francisco", "New York", "Austin", "Seattle", "Remote"]

st.title("💼 Employee Salary Predictor")
st.write("Upload your resume and fill the form below to predict your salary and see your ATS score.")

with st.form("salary_form"):
    resume_file = st.file_uploader("📄 Upload Resume (.pdf or .docx)", type=["pdf", "docx"], help="Used for ATS score")
    name = st.text_input("👤 Name")
    gender = st.selectbox("🚻 Gender", ["Male", "Female", "Other"])
    age = st.number_input("🎂 Age", min_value=18, max_value=65, value=25)
    years_exp = st.number_input("💼 Years of Total Experience", min_value=0, max_value=50, value=1)
    work_exp = st.number_input("🧾 Previous Work Experience (in years)", min_value=0, max_value=50, value=0)
    marital_status = st.selectbox("💍 Marital Status", ["Single", "Married"])
    hours_per_week = st.slider("⏱️ Hours per Week", 10, 80, 40)
    occupation = st.selectbox("💻 Current Occupation", occupations)
    applied_position = st.selectbox("📌 Applied Role", positions)
    place = st.selectbox("📍 Location", locations)

    submitted = st.form_submit_button("🚀 Predict Salary")

def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = " ".join(page.extract_text() or '' for page in reader.pages)
    elif file.name.endswith(".docx"):
        doc = Document(io.BytesIO(file.read()))
        text = " ".join([para.text for para in doc.paragraphs])
    return text.lower()

def calculate_ats_score(resume_text, position):
    resume_words = resume_text.split()
    position_words = position.lower().split()
    if not resume_words:
        return 0
    matches = sum(1 for word in position_words if word in resume_words)
    score = int((matches / len(position_words)) * 100)
    return min(score + random.randint(0, 20), 100)

def predict_salary(exp, work_exp, hours, place):
    base = 30000
    exp_bonus = exp * 1200
    work_bonus = work_exp * 800
    hours_bonus = hours * 60
    loc_bonus = {"San Francisco": 10000, "New York": 5000, "Austin": 2000, "Seattle": 3000, "Remote": 1500}
    return base + exp_bonus + work_bonus + hours_bonus + loc_bonus.get(place, 0)

if submitted:
    if not resume_file:
        st.error("Please upload a resume.")
    else:
        resume_text = extract_text(resume_file)
        ats_score = calculate_ats_score(resume_text, applied_position)
        salary = predict_salary(years_exp, work_exp, hours_per_week, place)

        st.success(f"💰 **Predicted Salary:** ${salary:,}")
        st.info(f"✅ **ATS Score:** {ats_score}%")
