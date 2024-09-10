import streamlit as st

# Page configuration
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

# Introduction Section
def introduction():
    st.write("")  # Adding vertical space
    col1, col2 = st.columns([3, 2])

    with col1:
        st.title("CareerCraft")
        st.header("Navigate the Job Market with Confidence!")

    with col2:
        st.markdown("""
        <p style="text-align: justify;">
        Introducing CareerCraft, an ATS-Optimized Resume Analyzer - your ultimate solution for optimizing job applications and accelerating career growth. 
        Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions. 
        From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market.
        Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success!
        </p>
        """, unsafe_allow_html=True)

        st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_column_width=True)
    st.write("")  # Adding vertical space


# Render the sections
introduction()

