# ATS Resume Expert – AI-Powered Resume Analysis & Matching 
ATS Resume Expert is a Streamlit-based AI-powered web app that helps job seekers optimize their resumes. It analyzes resumes against job descriptions using Google Gemini AI, providing ATS compatibility scores, keyword analysis, and expert HR evaluations to enhance hiring chances.

 # Features
🔹 AI-Powered Resume Analysis – Get expert feedback on your resume.

🔹 ATS Match Score – See how well your resume fits a job description.

🔹 Keyword Optimization – Identify missing keywords to improve ATS ranking.

🔹 PDF Resume Processing – Converts and analyzes PDF resumes.

🔹 User-Friendly UI – Built with Streamlit for easy interaction.

# Tech Stack

🔹 Python – Core language for backend logic.

🔹 Streamlit – Web framework for UI.

🔹 Google Gemini AI API – Provides AI-powered resume evaluation.

🔹 pdf2image & PIL – Converts PDFs to images for AI processing.

🔹 Base64 Encoding – Ensures smooth image handling.

 # How It Works
 
1️⃣ Upload Your Resume – Supports PDF format.

2️⃣ Enter Job Description – Paste the job description.

3️⃣ Choose Analysis Type:

🔹Analyze Resume – AI acts as an HR manager, evaluating strengths & weaknesses.
🔹Check Match Percentage – AI calculates your ATS compatibility score.

4️⃣ View AI Feedback – Get insights, missing keywords, and optimization tips.

# Installation & Setup

1️⃣ Clone the Repository
git clone [https://github.com/your-username/ats-resume-expert.git](https://github.com/Priya897908/ATS-System)

cd ATS-System

2️⃣ Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up API Key
Create a .env file in the root directory.
Add your Google Gemini API key inside the .env file:

🔹GOOGLE_API_KEY="AIzaSyBtov8fkffOjgesH0Tt9IUfiNBAidgWKTo"

5️⃣ Run the Application
streamlit run app.py











