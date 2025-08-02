import os
import streamlit as st

# Fix for libGL.so.1 error (needed by OpenCV on cloud)
os.system('apt-get update && apt-get install -y libgl1-mesa-glx')

from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np


# Load model
model = YOLO("best.pt")

st.title("🛰️ Falcon Object Detection App")

# Webcam or upload mode
mode = st.radio("Choose input source:", ("Upload Image", "Use Webcam"))

if mode == "Upload Image":
    img = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if img:
        image = Image.open(img)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        results = model.predict(image)
        result_img = results[0].plot()
        st.image(result_img, caption="Detected Objects")

else:
    run = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access webcam")
            break

        results = model.predict(frame)
        result_frame = results[0].plot()

        FRAME_WINDOW.image(result_frame, channels="BGR")

    else:
        cap.release()
