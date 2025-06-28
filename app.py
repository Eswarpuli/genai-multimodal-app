import streamlit as st
from PIL import Image
from gemini_api import generate_text, generate_caption
from google.generativeai import GenerativeModel

st.set_page_config(page_title="Gemini AI", layout="wide")

# --- Custom CSS for integrated input + file button ---
st.markdown("""
    <style>
    .input-container {
        position: relative;
        width: 100%;
    }
    .text-input {
        width: 100%;
        padding-right: 100px; /* Space for the button */
    }
    .file-upload-button {
        position: absolute;
        right: 0;
        top: 0;
        height: 100%;
        display: flex;
        align-items: center;
        padding: 0 15px;
        background: #f0f2f6;
        border-left: 1px solid #ccc;
        border-radius: 0 8px 8px 0;
        cursor: pointer;
    }
    .file-upload-button:hover {
        background: #e2e5e9;
    }
    /* Hide the default file uploader styling */
    div[data-testid="stFileUploader"] {
        width: auto !important;
    }
    div[data-testid="stFileUploader"] > section {
        padding: 0 !important;
        border: none !important;
    }
    div[data-testid="stFileUploader"] > label {
        display: none !important;
    }
    div[data-testid="stFileUploader"] button {
        background: none !important;
        border: none !important;
        box-shadow: none !important;
        color: inherit !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Gemini AI Multimodal Assistant</h1><hr>", unsafe_allow_html=True)

# --- Input with integrated file button ---
st.markdown('<div class="input-container">', unsafe_allow_html=True)

# Main text input
prompt = st.text_input(" ", placeholder="Ask anything...", label_visibility="collapsed", key="text_input", help=None)

# File uploader positioned absolutely over the text input
uploaded_file = st.file_uploader("📎", type=["jpg", "jpeg", "png"], label_visibility="collapsed", key="file_input")

st.markdown('</div>', unsafe_allow_html=True)

# --- Logic Handling ---
if prompt and not uploaded_file:
    with st.spinner("Generating text response..."):
        response = generate_text(prompt)
    st.success("Text Response:")
    st.write(response)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    question_about_image = st.text_input("Ask something about the image:")

    if question_about_image:
        with st.spinner("Generating response from image..."):
            model = GenerativeModel("gemini-2.5-flash-preview-04-17")
            response = model.generate_content([image, question_about_image])
            st.success("Response:")
            st.write(response.text)
    else:
        with st.spinner("Generating caption..."):
            caption = generate_caption(image)
            st.success("Image Caption:")
            st.write(caption)
