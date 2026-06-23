import streamlit as st
from PIL import Image
from transformers import pipeline


@st.cache_resource
def load_classifier():
    return pipeline(
        "image-classification",
        model="microsoft/resnet-50"
    )


def show_image_classifier():

    st.title("🖼️ AI Image Classifier")

    uploaded_file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        with st.spinner("Analyzing Image..."):

            classifier = load_classifier()

            results = classifier(image)

        prediction = results[0]["label"]
        confidence = results[0]["score"] * 100

        st.success(
            f"Prediction: {prediction}"
        )

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(
            int(confidence)
        )

        st.subheader("Top Predictions")

        for item in results[:5]:

            st.write(
                f"{item['label']} : {item['score']*100:.2f}%"
            )