import streamlit as st
from datetime import datetime


def get_response(prompt):

    user_input = prompt.lower().strip()

    # About Bot
    if any(word in user_input for word in [
        "who are you",
        "about you",
        "developer",
        "creator",
        "developed you"
    ]):
        return """
👋 Hello!

I am an AI Assistant developed by Viniksan.

🚀 Features:
• AI Chat Assistant
• Resume Analyzer
• Image Classifier
• Text Summarizer
• Sentiment Analysis
• Content Generator

🛠 Technologies:
• Python
• Streamlit
• SQLite
• Machine Learning
"""

    # Greetings
    elif any(word in user_input for word in [
        "hi",
        "hello",
        "hey"
    ]):
        return "👋 Hello! How can I help you today?"

    elif "how are you" in user_input:
        return "😊 I'm doing great. Thanks for asking."

    # Time & Date
    elif "time" in user_input:
        return f"🕒 Current Time: {datetime.now().strftime('%I:%M %p')}"

    elif "date" in user_input:
        return f"📅 Today's Date: {datetime.now().strftime('%d-%m-%Y')}"

    # Programming
    elif "python" in user_input:
        return """
🐍 Python

Python is one of the most popular programming languages.

Uses:
• AI
• Machine Learning
• Data Science
• Web Development
• Automation
"""

    elif "java" in user_input:
        return """
☕ Java

Java is an object-oriented programming language.

Uses:
• Android Apps
• Enterprise Software
• Backend Development
"""

    elif "html" in user_input:
        return """
🌐 HTML

HTML stands for HyperText Markup Language.

Used for creating website structure.
"""

    elif "css" in user_input:
        return """
🎨 CSS

CSS is used for styling web pages.
"""

    elif "javascript" in user_input:
        return """
⚡ JavaScript

JavaScript makes websites interactive.

Uses:
• Frontend Development
• Backend Development
"""

    elif "sql" in user_input:
        return """
🗄 SQL

SQL is used to manage databases.

Examples:
• MySQL
• PostgreSQL
• SQLite
"""

    # AI
    elif "artificial intelligence" in user_input or user_input == "ai":
        return """
🤖 Artificial Intelligence

AI enables machines to think and make decisions.

Examples:
• ChatGPT
• Self Driving Cars
• Face Recognition
"""

    elif "machine learning" in user_input:
        return """
🧠 Machine Learning

Machine Learning helps systems learn from data.

Applications:
• Predictions
• Recommendations
• Fraud Detection
"""

    elif "deep learning" in user_input:
        return """
🧠 Deep Learning

Deep Learning uses neural networks to solve
complex AI problems.
"""

    elif "data science" in user_input:
        return """
📊 Data Science

Data Science combines:

• Statistics
• Programming
• Machine Learning

to extract insights from data.
"""

    # Country
    elif "india" in user_input:
        return """
🇮🇳 India

Capital: New Delhi

Population: 1.4+ Billion

India is the world's largest democracy.

Famous Places:
• Taj Mahal
• Goa
• Kerala
• Red Fort
"""

    # Resume
    elif "resume" in user_input:
        return """
📄 Resume Tips

• Add Projects
• Add Certifications
• Highlight Skills
• Use Professional Format
• Keep It Simple
"""

    # Skills
    elif "skill" in user_input:
        return """
💼 Top Skills

Programming:
• Python
• Java
• SQL

Web:
• HTML
• CSS
• JavaScript

AI:
• Machine Learning
• Deep Learning

Tools:
• Git
• GitHub
• Streamlit
"""

    # Streamlit
    elif "streamlit" in user_input:
        return """
🚀 Streamlit

Streamlit is a Python framework for building
web apps quickly.
"""

    elif "thank" in user_input:
        return "😊 You're welcome. Happy coding!"

    else:
        return f"""
🤖 Offline Assistant

Question:
{prompt}

Currently I support:

• Python
• Java
• HTML
• CSS
• JavaScript
• SQL
• AI
• Machine Learning
• Data Science
• Streamlit
• Resume Tips
• Skills
• India

For real AI answers, connect Gemini API.
"""


def show_chatbot():

    st.title("🤖 AI Chat Assistant")

    st.caption("Developed by Viniksan")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat History
    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    st.markdown("### 💡 Recommended Questions")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🐍 Python"):
            st.session_state.selected_prompt = "python"

        if st.button("🇮🇳 India"):
            st.session_state.selected_prompt = "india"

        if st.button("🤖 AI"):
            st.session_state.selected_prompt = "artificial intelligence"

    with col2:
        if st.button("📊 Data Science"):
            st.session_state.selected_prompt = "data science"

        if st.button("🧠 Machine Learning"):
            st.session_state.selected_prompt = "machine learning"

        if st.button("🚀 Streamlit"):
            st.session_state.selected_prompt = "streamlit"

    with col3:
        if st.button("💼 Skills"):
            st.session_state.selected_prompt = "skills"

        if st.button("📄 Resume Tips"):
            st.session_state.selected_prompt = "resume"

        if st.button("👨‍💻 About Bot"):
            st.session_state.selected_prompt = "who are you"

    user_input = st.chat_input("Ask anything...")

    if "selected_prompt" in st.session_state:
        user_input = st.session_state.selected_prompt
        del st.session_state.selected_prompt

    if user_input:

        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        response = get_response(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.rerun()

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()