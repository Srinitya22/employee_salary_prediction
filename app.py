import streamlit as st
import fitz  # PyMuPDF

# Page configuration
st.set_page_config(page_title="Resume Analyzer 🇮🇳", page_icon="🧾", layout="centered")

# App title
st.title("🧾 Indian Resume Analyzer")
st.markdown("Upload your **PDF resume** and get an estimated ATS score!")

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload your resume (PDF only)", type=["pdf"])

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_pdf):
    text = ""
    with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# If file is uploaded
if uploaded_file:
    st.success("✅ PDF uploaded successfully!")

    # Extract text
    extracted_text = extract_text_from_pdf(uploaded_file)

    # Show extracted text
    st.subheader("📄 Extracted Resume Content:")
    st.text_area("Text Preview", extracted_text, height=300)

    # Dummy ATS score (just for demo)
    score = min(100, len(extracted_text) // 20 + 35)
    st.subheader("📊 ATS Score Estimate:")
    st.progress(score / 100)
    st.success(f"🎯 Your estimated ATS score is: **{score} / 100**")

else:
    st.info("Please upload a PDF file to begin.")

# Footer
st.markdown("---")
st.markdown("🛠️ Made with ❤️ by V.Srinitya for Indian job seekers | Supports only **PDF** resumes for now.")
