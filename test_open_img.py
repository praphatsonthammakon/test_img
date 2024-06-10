import streamlit as st
import cv2
import numpy as np

st.title("Image Uploader")

img_file = st.file_uploader("เปิดไฟล์ภาพ")

if img_file is not None:
    # Convert the file to an OpenCV image
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Resize the image to 1536x2048
    resized_img = cv2.resize(img, (2048, 1536))
    
    # Get the dimensions of the resized image
    h, w, c = resized_img.shape
    
    # Display the resized image
    st.image(resized_img, channels="BGR")
    
    # Display image details
    st.text(f"ชื่อไฟล์: {img_file.name}")
    st.text(f"ขนาดภาพ: {w} x {h} x {c}")
