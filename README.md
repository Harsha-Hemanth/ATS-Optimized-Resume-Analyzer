# ✨ ATS Optimized Resume Analyzer ✨
This AI-powered Resume Analyzer helps users optimize their resumes for Applicant Tracking Systems (ATS) by providing personalized feedback and insights using Google Generative AI. Simply upload your resume, and the application will analyze its content and suggest improvements to boost its ATS performance.

## 🚀 Features
- AI-Powered Insights: Get feedback on your resume content using Google Generative AI.
- PDF Upload: Upload your resume in PDF format for analysis.
- Keyword Matching: Automatically checks your resume for important keywords related to the job role.
- ATS Optimization Tips: Provides suggestions to make your resume more ATS-friendly.
- Skill Scoring: Analyzes the skills section and offers scoring based on relevance.
- Interactive UI: Easy-to-use interface built using Streamlit.
- Privacy Focused: Your data is not stored, ensuring privacy and security.
## 📋 Prerequisites
Make sure you have the following installed:

- Python 3.11 or higher
- Streamlit: Framework for building interactive web apps
- Google Generative AI: For AI-powered resume analysis
- PyPDF2: To read and extract text from PDF files
- python-dotenv: To load environment variables securely
## 🛠️ Installation

1. Clone the repository:
  
    ```bash
    git clone https://github.com/yourusername/ATS-Optimized-Resume-Analyzer.git
    cd ATS-Optimized-Resume-Analyzer

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

4. Set up your environment variables:

- Create a .env file in the root directory and add your Google Generative AI API key.
    ```bash
    GOOGLE_API_KEY=your_api_key_here

## 📜 Usage
1. Run the Streamlit application:

    ```bash
    streamlit run app.py
    
2. Open your browser and go to http://localhost:8501.

3. Upload your resume in PDF format and let the analyzer do its magic. It will display the following information:

- ATS score
- Keyword analysis
- Suggestions for improvement
  
## 🧰 Technologies Used
- Streamlit: Web application framework
- Google Generative AI: Natural language processing for resume insights
- PyPDF2: PDF parsing library
- Python-dotenv: For environment variable management


## 🤖 How It Works
1. Upload PDF: Users upload their resume as a PDF file.
2. Text Extraction: The PyPDF2 library extracts the text from the PDF.
3. AI Analysis: The extracted text is analyzed using Google Generative AI for keyword relevance and ATS optimization.
4. Feedback: The system provides actionable feedback for improving the resume.
## 💡 Future Enhancements
- Add support for multiple file types (e.g., .docx).
- Include job description matching for targeted resume improvements.
- Integrate more AI models for deeper analysis.
## 👤 Author
- **[Harsha Hemanth](https://github.com/Harsha-Hemanth)** - Developer & Maintainer
