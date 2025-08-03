import streamlit as st
import cv2
import numpy as np

st.set_page_config(page_title="Webcam Access App", layout="centered")
st.title("🎥 Webcam Access in Streamlit")

# Checkbox to enable webcam
use_webcam = st.checkbox("Start Webcam")

# Placeholder for camera feed
frame_placeholder = st.empty()

if use_webcam:
    cap = cv2.VideoCapture(0)  # Try 1 or 2 if 0 doesn't work

    if not cap.isOpened():
        st.error("❌ Failed to access webcam. Try restarting your browser or using a different camera index.")
    else:
        st.info("✅ Webcam started. Click the checkbox to stop.")

        while use_webcam:
            ret, frame = cap.read()
            if not ret:
                st.warning("⚠️ Couldn't read from webcam.")
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame, channels="RGB", use_container_width=True)

            # Stop loop if checkbox is turned off
            if not st.session_state.get("Start Webcam", True):
                break

        cap.release()
        st.success("✅ Webcam stopped.")
