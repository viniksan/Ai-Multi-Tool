import streamlit as st
from textblob import TextBlob


def show_sentiment():

    st.title("😊 Sentiment Analysis")

    text = st.text_area(
        "Enter Text"
    )

    if st.button("Analyze Sentiment"):

        if text:

            polarity = TextBlob(
                text
            ).sentiment.polarity

            if polarity > 0:

                st.success(
                    "Positive 😊"
                )

            elif polarity < 0:

                st.error(
                    "Negative 😔"
                )

            else:

                st.info(
                    "Neutral 😐"
                )

        else:

            st.warning(
                "Enter some text"
            )