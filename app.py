from dotenv import load_dotenv

load_dotenv()

import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_text, pdf_content, prompt):
    """Generates a response from the Gemini API"""
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated to latest model
    response = model.generate_content([input_text, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    """Converts the first page of a PDF to a base64-encoded image for processing"""
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        if not images:
            raise ValueError("PDF conversion failed, no images extracted.")

        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        return [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.set_page_config(page_title="ATS Resume Expert", layout="centered")
st.title("ATS Resume Tracking System")

# User Input
input_text = st.text_area("Enter Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    st.success("✅ Resume Uploaded Successfully!")

# Prompts
input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Review the provided resume against the job description and provide an evaluation. 
Highlight strengths, weaknesses, and whether the candidate's profile aligns with the role.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with expertise in resume analysis. 
Evaluate the resume against the job description and provide a percentage match. 
Your response should include: 
1. Match percentage.
2. Missing keywords.
3. Final evaluation.
"""

# Buttons
col1, col2 = st.columns(2)

with col1:
    submit1 = st.button("Analyze Resume")

with col2:
    submit3 = st.button("Check Match Percentage")

# Processing Requests
if submit1 or submit3:
    if uploaded_file:
        try:
            pdf_content = input_pdf_setup(uploaded_file)
            prompt = input_prompt1 if submit1 else input_prompt3
            response = get_gemini_response(input_text, pdf_content, prompt)
            st.subheader("AI Evaluation")
            st.success("✅ Analysis Complete!")
            st.write(response)
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please upload your resume before proceeding.")
