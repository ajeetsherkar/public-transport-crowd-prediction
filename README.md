# AI-Based Public Transport Crowding Prediction System 🚍

## Overview
This project is an AI-powered Smart City solution that predicts public transport crowd levels
(Low, Medium, High) using machine learning. It helps commuters plan travel better and assists
transport authorities in managing congestion.

## Problem Statement
Urban public transport systems often experience unpredictable crowding, leading to discomfort,
delays, and safety concerns. There is a need for a predictive system that estimates crowd levels
in advance using historical and contextual data.

## Solution
We developed a machine learning–based crowd prediction system that analyzes:
- Route information
- Time of travel
- Day type (weekday/weekend)
- Weather conditions
- Holiday indicators

The trained model is deployed using a FastAPI backend and accessed via a Streamlit dashboard
for real-time predictions.

## Technology Stack
- Python
- Pandas, NumPy
- Scikit-learn (Random Forest)
- FastAPI (Backend API)
- Streamlit (Frontend UI)
- Git & GitHub (Version Control)

## Machine Learning Approach
- Problem Type: Multi-class Classification
- Model: Random Forest Classifier
- Accuracy: ~75% on realistic synthetic data
- Feature Importance analysis used for interpretability

## System Architecture
Streamlit UI → FastAPI Backend → ML Model → Crowd Prediction

## How to Run the Project
1. Clone the repository
2. Install dependencies:
pip install -r requirements.txt
3. Start the backend:
   uvicorn app.main:app --reload
4. Start the frontend:
   streamlit run ui/app.py
5. Open browser at:
   [text](http://localhost:8501)


## Future Enhancements
- Integration with real-time transport data
- GPS and IoT-based crowd sensing
- Camera-based crowd detection
- City-wide scalability across multiple transport modes

## License
This project was developed for educational and hackathon purposes.