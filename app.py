import streamlit as st
from PIL import Image
from gemini_utils import generate_text, generate_caption

st.set_page_config(page_title="Gemini AI - MultiModal", layout="centered")

st.title("🧠 Gemini AI - Multimodal Generator")

option = st.selectbox("Choose a Mode", ["Text to Text", "Image to Text"])

if option == "Text to Text":
    prompt = st.text_area("Enter your prompt:")
    if st.button("Generate Text"):
        if prompt.strip() == "":
            st.warning("Please enter some text.")
        else:
            response = generate_text(prompt)
            st.success(response)

elif option == "Image to Text":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)  # Ensures it's a PIL image
        st.image(image, caption="Uploaded Image", use_container_width=True)
        if st.button("Generate Caption"):
            response = generate_caption(image)  # Pass PIL Image
            st.success(response)
