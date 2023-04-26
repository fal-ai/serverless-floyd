from fal_serverless import isolated, cached

import streamlit as st
import io
from PIL import Image
import base64
import time

st.title("Welcome to deepfloyd on fal-serverless")

requirements = [
    "deepfloyd_if==1.0.0",
    "xformers==0.0.16",
    "git+https://github.com/openai/CLIP.git",
]


@cached
def setup():
    return


@isolated(requirements=requirements, machine_type="M")
def generate_image():
    a = setup()
    return a


with st.form(key="my_form"):
    print("Starting", time.time())
    text_input = st.text_input(
        label="Enter a prompt here to generate an image with Deep Floyd"
    )
    submit_button = st.form_submit_button(label="Generate")

if submit_button:
    img64 = generate_image(text_input)
    image = Image.open(io.BytesIO(base64.b64decode(img64)))

    st.image(image)
