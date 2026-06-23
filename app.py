import streamlit as st
from streamlit_option_menu import option_menu

from database_utils.db import create_database
from auth.login import login_user
from auth.register import register_user

from modules.chatbot import show_chatbot
from modules.image_classifier import show_image_classifier
from modules.resume_analyzer import show_resume_analyzer
from modules.summarizer import show_summarizer
from modules.sentiment import show_sentiment
from modules.content_generator import show_content_generator

# ---------------- DATABASE ----------------

create_database()

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Multi Tool Platform",
    page_icon="🤖",
    layout="wide"
)
# ---------------- LOAD CSS ----------------

try:
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except Exception as e:
    st.error(f"CSS Error: {e}")

# ---------------- SESSION STATE ----------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- LOGIN PAGE ----------------

def login_page():

    st.title("🤖 AI Multi Tool Platform")
    st.subheader("Login or Register")

    tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])

    with tab1:

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button("Login", use_container_width=True):

            if login_user(username, password):

                st.session_state.logged_in = True
                st.session_state.username = username

                st.success("Login Successful")
                st.rerun()

            else:
                st.error("Invalid Username or Password")

    with tab2:

        new_user = st.text_input(
            "Create Username",
            key="register_username"
        )

        new_pass = st.text_input(
            "Create Password",
            type="password",
            key="register_password"
        )

        if st.button("Register", use_container_width=True):

            if register_user(new_user, new_pass):
                st.success("Account Created Successfully")
            else:
                st.error("Username Already Exists")

# ---------------- DASHBOARD ----------------

def dashboard():

    st.title("🚀 AI Multi Tool Platform")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Tools", "6")

    with col2:
        st.metric("Status", "Online")

    with col3:
        st.metric("User", st.session_state.username)

    st.divider()

    st.success(
        f"Welcome {st.session_state.username}!"
    )

    st.info(
        """
🤖 Chat Assistant

🖼️ Image Classifier

📄 Resume Analyzer

📝 Text Summarizer

😊 Sentiment Analysis

✍️ Content Generator
"""
    )

# ---------------- MAIN PAGE ----------------

def main_page():

    with st.sidebar:

        st.title("🤖 AI Platform")

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Chat Assistant",
                "Image Classifier",
                "Resume Analyzer",
                "Text Summarizer",
                "Sentiment Analysis",
                "Content Generator"
            ],
            icons=[
                "house",
                "chat-dots",
                "image",
                "file-earmark-person",
                "file-text",
                "emoji-smile",
                "pencil-square"
            ],
            default_index=0
        )

        st.divider()

        st.success(
            f"👤 {st.session_state.username}"
        )

        if st.button(
            "Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()

    if selected == "Dashboard":
        dashboard()

    elif selected == "Chat Assistant":
        show_chatbot()

    elif selected == "Image Classifier":
        show_image_classifier()

    elif selected == "Resume Analyzer":
        show_resume_analyzer()

    elif selected == "Text Summarizer":
        show_summarizer()

    elif selected == "Sentiment Analysis":
        show_sentiment()

    elif selected == "Content Generator":
        show_content_generator()

# ---------------- START APP ----------------

if st.session_state.logged_in:
    main_page()
else:
    login_page()