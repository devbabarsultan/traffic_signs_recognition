"""
Traffic Signs Recognition - Simple Streamlit UI
Single image prediction via FastAPI backend at localhost:8000
"""

import streamlit as st
import requests
from PIL import Image
import io
import json
import time

st.set_page_config(
    page_title="Traffic Signs Recognition",
    layout="centered"
)

# API Configuration
API_URL = "http://localhost:8000/predict"

def check_api_health():
    """Check if FastAPI backend is running"""
    try:
        response = requests.get("http://localhost:8000/health", timeout=3)
        return response.status_code == 200
    except:
        return False

def predict_image(image_file):
    """Send image to FastAPI backend for prediction"""
    try:
        files = {
            'file': (
                image_file.name,
                image_file.getvalue(),
                image_file.type or 'image/jpeg'
            )
        }
        
        response = requests.post(
            API_URL,
            files=files,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f'API Error: {response.status_code}'}
            
    except requests.exceptions.ConnectionError:
        return {'error': 'Cannot connect to backend. Is FastAPI running on port 8000?'}
    except requests.exceptions.Timeout:
        return {'error': 'Request timed out. Please try again.'}
    except Exception as e:
        return {'error': f'Unexpected error: {str(e)}'}
    
timer = 0

def main():
    """Main application"""
    
    st.title("Traffic Signs Recognition")
    st.markdown("Upload a traffic sign image for recognition")
    st.markdown("---")
    
    if not check_api_health():
        st.error("Backend not available. Please start FastAPI server on port 8000.")
        st.info("Run: `uvicorn fastapi-backend.main:app --reload --port 8000`")
        return
    else:
        st.success("Backend connected")
    
    st.markdown("---")
    
    uploaded_file = st.file_uploader(
        "Choose a traffic sign image...",
        type=["jpg", "jpeg", "png", "bmp", "webp"],
        help="Supported formats: JPG, PNG, BMP, WEBP"
    )
    
    if uploaded_file is not None:

        col1, col2 = st.columns(2)
        
        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            st.write("")
            st.write("")
            if st.button("Predict", type="primary", use_container_width=True):
                with st.spinner("Analyzing image..."):
                    starting_time = time.time()
                    result = predict_image(uploaded_file)
                    global timer
                    timer = time.time()  - starting_time
                    display_prediction(result)
    
    st.markdown("---")
    st.caption("Powered by FastAPI Backend | Streamlit Frontend")

def display_prediction(result):
    """Display prediction results"""
    
    if 'error' in result:
        st.error(f"{result['error']}")
        return
    
    # Extract prediction
    class_name = result.get('Prediction', 'Unknown')
    confidence = result.get('Score', 0.0)
    processing_time = timer
    
    # Display results
    st.markdown("---")
    st.subheader("Prediction Result")
    
    # Confidence color
    color = "green" if confidence > 0.7 else "orange" if confidence > 0.4 else "red"
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        ### {class_name}
        <span style="color:{color}; font-size: 16px;">{confidence:.2%}</span>
        """, unsafe_allow_html=True)
        
        st.progress(confidence)
    
    with col2:
        st.metric("Confidence Score", f"{confidence:.1%}")
        st.metric("Processing Time", f"{processing_time:.3f}s")
    
    with st.expander("📝 Raw API Response"):
        st.json(result)

if __name__ == "__main__":
    main()