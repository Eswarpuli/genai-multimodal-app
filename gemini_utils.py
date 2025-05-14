# gemini_utils.py
import google.generativeai as genai
from PIL import Image

# Configure your actual API key
genai.configure(api_key="AIzaSyDBxoq_wptXGTWQ_Y38LTsJcMivGkwyhG8")

# Text-to-Text generation
def generate_text(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
    response = model.generate_content(prompt)
    return response.text

# Image-to-Text generation
def generate_caption(image: Image.Image):
    model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
    response = model.generate_content([
        image,
        "Describe this image in detail"
    ])
    return response.text
