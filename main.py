from PIL import Image
import os
import numpy as np 
import streamlit as st
from streamlit_image_comparison import image_comparison
import cv2

navbar = st.container()

header = st.container()

upload = st.container()

dropdown= st.container()

slider = st.container()



with header:
    st.title("Image Super Resolutionn")

upload_path = "uploads/"

with upload:
    uploadFile=st.file_uploader("choose an image ")
    if uploadFile is not None:
        with open(os.path.join(upload_path,uploadFile.name),"wb") as f:
            f.write((uploadFile).getbuffer())
        with st.spinner(f"Working... 💫"):
            uploaded_image = os.path.abspath(os.path.join(upload_path,uploadFile.name))

    def load_image(img):
        im = Image.open(img)
        image = np.array(im)
        return image

    if uploadFile is not None:
        img = load_image(uploadFile)
        st.image(img)   
        st.write("image uploaded successfully")
    else:
        st.write("image not uploaded successfully")


with dropdown:
    st.markdown("""
    <style>
    .big-font {
    font-size:50px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Choose Model for Image Super Resolution     !!</p>', unsafe_allow_html=True)
    model_name = st.radio("", ('ESRGAN model ✅', 'PSNR-oriented model ✅'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)





with slider:
    st.markdown("LR to HR Image Comparison")
    image_comparison(
        img1="assets/stivlr.jpg",
        img2="assets/stivhr.jpg",
        label1="Before",
        label2="After",
    )