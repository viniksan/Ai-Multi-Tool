import streamlit as st
import pdfplumber


def extract_text(pdf_file):

    text = ""

    with pdfplumber.open(pdf_file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text


def show_resume_analyzer():

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    if uploaded_file is not None:

        text = extract_text(uploaded_file)

        keywords = [
            "python",
            "sql",
            "machine learning",
            "streamlit",
            "data analysis"
        ]

        found_skills = []

        score = 0

        for skill in keywords:

            if skill.lower() in text.lower():

                found_skills.append(skill)

                score += 20

        st.metric(
            "Resume Score",
            f"{score}/100"
        )

        st.subheader("Skills Found")

        if found_skills:

            for skill in found_skills:
                st.success(skill)

        else:
            st.warning("No matching skills found")

        st.subheader("Resume Feedback")

        if score >= 80:

            st.success(
                """
Strong resume with good technical skills.

Recommended Roles:
• Data Analyst
• Machine Learning Intern
• Python Developer
"""
            )

        elif score >= 60:

            st.warning(
                """
Good resume.

Suggestions:
• Add more projects
• Add certifications
• Improve achievements
"""
            )

        else:

            st.error(
                """
Resume needs improvement.

Suggestions:
• Learn Python
• Learn SQL
• Build Projects
• Add Certifications
"""
            )