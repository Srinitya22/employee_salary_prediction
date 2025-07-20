# 💼 Employee Salary Prediction using Machine Learning & ATS Score 💰📄

An ML powered web application that predicts an employee’s annual salary (in ₹ INR) based on their experience, job role, location, and other factors. The app also evaluates resume strength using ATS (Applicant Tracking System) logic by checking for relevant keywords — helping job seekers optimize their resumes effectively.

---

## 🎯 Objective

To create an interactive salary prediction and resume scoring tool using machine learning principles and a user-friendly Streamlit interface. This app empowers job seekers with salary expectations and resume feedback, particularly within the Indian job market.

---

## 🔍 Features

- Predict annual salary in Indian Rupees (₹) 💰
- Upload your resume (PDF) and get an ATS score 📄
- Mobile-responsive UI with a pastel gradient background 🎨
- User inputs include:
  - Name
  - Experience
  - Marital status
  - Work hours per week
  - Current occupation & applied role
  - Location (Indian cities)
  - Education level
- ATS score based on relevant industry keywords (e.g., Python, SQL)
- Friendly, informative feedback messages based on predictions ✅

---

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** – for building the interactive UI
- **PyPDF2** – to read and parse uploaded PDF resumes
- **Babel** – to format salary in Indian currency style
- **Machine Learning** (manual logic / optional .pkl usage)
- **HTML + CSS** – for styling the UI components

---

## How It Works
Uses a rule-based model (or optionally trained ML .pkl) to estimate salary.

Resume ATS score is calculated by matching keywords like python, sql, machine learning, etc.

The logic considers job role, location (cost of living), experience, and hours per week to compute a tailored salary.

Clean and modern UI enhances user experience across devices.

## 📌 Use Case
Ideal for:

Fresh graduates and job seekers estimating expected salaries

Candidates optimizing resumes for tech roles

HR teams building quick benchmarks

## 📈 Example Output
Predicted Salary: ₹4,50,000

ATS Resume Score: 67%

Feedback: ✅ Great! Your resume is well-optimized.

## 🙋‍♀️ Creator
<div align="center"> <b>Made with 💖 by <span style="color:#d6336c;">V. Srinitya Gargeyi</span></b> <br><br>
Student at GITAM(Deemed to be University),ECE(AIML)
</div>

## 📚 References
Streamlit Docs

PyPDF2 Documentation

Babel - Python i18n Library

Indian IT salary trend reports

Resume keyword guides (Naukri, LinkedIn, Indeed)


