# Zed Math AI

This project is an interactive AI-powered application using a webcam to recognize hand gestures and trigger an AI model to solve math problems based on specific gestures. It integrates OpenCV for webcam capture, cvzone for hand tracking, Streamlit for a user interface, and Google’s Generative AI for answering math problems.

## Features

- **Hand Gesture Recognition**: Recognizes specific hand gestures to draw on a virtual canvas.
- **AI Math Problem Solver**: Sends captured gestures to an AI model, triggering it to solve math problems.
- **Real-Time Interface**: Displays live video feed, gesture-based drawing, and AI-generated responses.

## Requirements

- Python 3.7+
- Webcam-enabled device

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python -m venv env
    source env/bin/activate      # On macOS/Linux
    .\env\Scripts\activate       # On Windows
    ```

3. **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your API key for Google Generative AI**:
   - Add your Google Generative AI API key where `genai.configure(api_key="YOUR_API_KEY")` appears in the code.

5. **Place the Hand Detection Image**:
   - Ensure `Zed Math AI.png` is in the project directory, or replace with a suitable image path.

## Libraries Required

Here's a list of libraries used in this project:
- `cv2` (OpenCV) for real-time video capture
- `cvzone` for hand gesture detection
- `streamlit` for creating the user interface
- `google.generativeai` for AI-driven responses
- `PIL` (Pillow) for image handling
- `numpy` for array operations

If you don't have `cvzone` installed, you can get it directly:
```bash
pip install cvzone
