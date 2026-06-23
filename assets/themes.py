import streamlit as st


def dashboard_theme():
    st.markdown("""
    <style>
    .stApp{
    background:linear-gradient(-45deg,#0f172a,#1e3a8a,#2563eb,#0f172a);
    background-size:400% 400%;
    animation:gradient 12s ease infinite;
    }

    @keyframes gradient{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
    }
    </style>
    """, unsafe_allow_html=True)


def chatbot_theme():
    st.markdown("""
    <style>
    .stApp{
    background:#050816;
    }

    .stApp::before{
    content:'';
    position:fixed;
    width:500px;
    height:500px;
    background:#00ffff33;
    border-radius:50%;
    filter:blur(120px);
    animation:move1 10s infinite alternate;
    }

    @keyframes move1{
    from{transform:translate(0,0);}
    to{transform:translate(400px,200px);}
    }
    </style>
    """, unsafe_allow_html=True)


def image_theme():
    st.markdown("""
    <style>
    .stApp{
    background:linear-gradient(
    135deg,
    #0f172a,
    #581c87,
    #312e81
    );
    background-size:300% 300%;
    animation:bgmove 10s infinite;
    }

    @keyframes bgmove{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
    }
    </style>
    """, unsafe_allow_html=True)


def resume_theme():
    st.markdown("""
    <style>
    .stApp{
    background:linear-gradient(
    135deg,
    #111827,
    #1f2937,
    #374151
    );
    }
    </style>
    """, unsafe_allow_html=True)


def summarizer_theme():
    st.markdown("""
    <style>
    .stApp{
    background:linear-gradient(
    135deg,
    #052e16,
    #166534,
    #22c55e
    );
    background-size:300% 300%;
    animation:greenbg 10s infinite;
    }

    @keyframes greenbg{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
    }
    </style>
    """, unsafe_allow_html=True)


def sentiment_theme():
    st.markdown("""
    <style>
    .stApp{
    background:#0f172a;
    animation:sentimentbg 8s infinite;
    }

    @keyframes sentimentbg{
    0%{background:#0f172a;}
    50%{background:#1e293b;}
    100%{background:#0f172a;}
    }
    </style>
    """, unsafe_allow_html=True)


def content_theme():
    st.markdown("""
    <style>
    .stApp{
    background:linear-gradient(
    -45deg,
    #0f172a,
    #78350f,
    #f59e0b,
    #0f172a
    );
    background-size:400% 400%;
    animation:goldbg 12s ease infinite;
    }

    @keyframes goldbg{
    0%{background-position:0% 50%;}
    50%{background-position:100% 50%;}
    100%{background-position:0% 50%;}
    }
    </style>
    """, unsafe_allow_html=True)