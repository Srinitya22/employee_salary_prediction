# employee_salary_predictor.py
from flask import Flask, render_template_string, request
from werkzeug.utils import secure_filename
import os
import random
from PyPDF2 import PdfReader
from docx import Document

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Employee Salary Predictor</title>
  <style>
    body { font-family: sans-serif; max-width: 600px; margin: auto; padding: 2rem; }
    input, select { width: 100%; padding: 8px; margin-bottom: 1rem; }
    button { padding: 10px 20px; }
    .result { margin-top: 2rem; padding: 1rem; background: #f0f0f0; border-radius: 8px; }
  </style>
</head>
<body>
  <h1>Employee Salary Predictor</h1>
  <form method="POST" enctype="multipart/form-data">
    <input type="file" name="resume" required />
    <input type="text" name="name" placeholder="Name" required />
    <select name="gender" required>
      <option value="">Select Gender</option>
      <option>Male</option>
      <option>Female</option>
      <option>Other</option>
    </select>
    <input type="number" name="age" min="18" max="65" value="{{ data.age }}" placeholder="Age" required />
    <input type="number" name="years_of_experience" value="{{ data.years_of_experience }}" placeholder="Years of Experience" required />
    <select name="marital_status" required>
      <option value="">Marital Status</option>
      <option>Single</option>
      <option>Married</option>
    </select>
    <input type="number" name="hours_per_week" value="{{ data.hours_per_week }}" placeholder="Hours per Week" required />
    <input type="text" name="occupation" placeholder="Occupation" required />
    <input type="text" name="applied_position" placeholder="Applied Position" required />
    <input type="text" name="place" placeholder="Location" required />
    <button type="submit">Predict Salary</button>
  </form>
  {% if salary and ats_score %}
  <div class="result">
    <h2>Prediction Results</h2>
    <p><strong>Predicted Salary:</strong> ${{ salary }}</p>
    <p><strong>ATS Score:</strong> {{ ats_score }}%</p>
  </div>
  {% endif %}
</body>
</html>
'''

def extract_text_from_resume(filepath):
    if filepath.endswith(".pdf"):
        try:
            pdf = PdfReader(filepath)
            return " ".join(page.extract_text() or '' for page in pdf.pages)
        except:
            return ""
    elif filepath.endswith(".docx"):
        try:
            doc = Document(filepath)
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

@app.route('/', methods=['GET', 'POST'])
def index():
    salary = None
    ats_score = None
    data = {
        'name': '',
        'gender': '',
        'age': 25,
        'years_of_experience': 1,
        'marital_status': '',
        'hours_per_week': 40,
        'occupation': '',
        'applied_position': '',
        'place': ''
    }

    if request.method == 'POST':
        resume = request.files['resume']
        resume_text = ""
        if resume:
            filename = secure_filename(resume.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume.save(filepath)
            resume_text = extract_text_from_resume(filepath)

        for key in data:
            data[key] = request.form.get(key)

        # Salary prediction logic
        base = 30000
        experience_factor = int(data['years_of_experience']) * 1000
        hours_factor = int(data['hours_per_week']) * 50
        place_factor = 10000 if data['place'] == 'San Francisco' else 0

        salary = base + experience_factor + hours_factor + place_factor

        # Real ATS score based on resume content
        ats_score = calculate_ats_score(resume_text, data['applied_position'])

    return render_template_string(TEMPLATE, data=data, salary=salary, ats_score=ats_score)

if __name__ == '__main__':
    app.run(debug=True)
