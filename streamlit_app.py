import cv2
import streamlit as st
from ultralytics import YOLO

from utils.empty_shelf_detector_model import EmptyShelfDetectorModel
from utils.logging_table import LoggingTable

def toggle_webcam():
    if st.session_state.is_webcam_started:
        cap.release()
        
    st.session_state.is_webcam_started = not st.session_state.is_webcam_started
    
def get_available_webcams(max_webcams=5):
    available_webcams = []
    
    for i in range(max_webcams):
        try:
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available_webcams.append((f"Webcam {i}", i))
                cap.release()
        except Exception as e:
            pass
        
    return available_webcams
    
cap = None
col1, col2 = st.columns(2)
empty_shelf_detector = EmptyShelfDetectorModel(YOLO('./model/model.pt'))

if 'is_webcam_started' not in st.session_state:
    st.session_state.is_webcam_started = False

with col1:
    st.title("Shelfie")
    
    webcam_list = get_available_webcams()

    if not webcam_list:
        st.write("No webcams found.")
    else:
        selected_webcam = st.selectbox("Select a Webcam", webcam_list, format_func=lambda x: x[0])

        webcam_text, webcam_id = selected_webcam
        
    st.button('Start Webcam' if not st.session_state.is_webcam_started else 'Stop Webcam', on_click=toggle_webcam)
    
    frame_placeholder = st.empty()

with col2:
    logging_table = LoggingTable(st.empty())
    logging_table.get_table()

if st.session_state.is_webcam_started:
    cap = cv2.VideoCapture(webcam_id)
    
    while st.session_state.is_webcam_started:
        ret, frame = cap.read()

        if not ret:
            st.error("Error accessing webcam.")
            break
        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        annotated_frame = empty_shelf_detector.detect(frame_rgb)
        detected_objects = empty_shelf_detector.count_detected_objects()
        
        logging_table.add_rows([str(detected_objects) + " empty product(s) detected."])
        frame_placeholder.image(annotated_frame, channels="RGB")