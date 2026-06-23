import streamlit as st


def show_summarizer():

    st.title("📝 Text Summarizer")

    text = st.text_area(
        "Paste Text Here",
        height=250
    )

    if st.button("Summarize"):

        if text:

            sentences = text.split(".")

            summary = ".".join(
                sentences[:3]
            )

            st.subheader("Summary")

            st.success(summary)

        else:

            st.warning("Enter some text")