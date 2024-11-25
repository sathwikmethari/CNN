@echo off
pip install -r requirements.txt
streamlit run cnn.py
start "" http://localhost:8501
