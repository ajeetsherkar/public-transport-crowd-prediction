import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Public Transport Crowd Prediction",
    layout="centered"
)

# Title and description
st.title("🚍 Public Transport Crowd Prediction")
st.caption("AI-powered Smart City Solution for Public Transport Crowding")

st.divider()

# -------- USER INPUTS --------
route_id = st.selectbox(
    "Select Route",
    [f"R{i}" for i in range(1, 21)]
)

hour = st.slider(
    "Hour of Travel",
    min_value=0,
    max_value=23,
    value=9
)

day_type = st.selectbox(
    "Day Type",
    ["Weekday", "Weekend"]
)

is_holiday = st.selectbox(
    "Is it a Holiday?",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Rain"]
)

st.divider()

# -------- PREDICTION BUTTON --------
if st.button("Predict Crowd Level"):
    payload = {
        "route_id": route_id,
        "hour": hour,
        "day_type": day_type,
        "is_holiday": is_holiday,
        "weather": weather
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=5
        )

        if response.status_code == 200:
            result = response.json()
            crowd_level = result["predicted_crowd_level"]

            if crowd_level == "High":
                st.error(f"🚨 Crowd Level: {crowd_level}")
            elif crowd_level == "Medium":
                st.warning(f"⚠️ Crowd Level: {crowd_level}")
            else:
                st.success(f"✅ Crowd Level: {crowd_level}")
        else:
            st.error("Backend returned an error.")

    except Exception:
        st.error("❌ Could not connect to backend API. Make sure FastAPI is running.")

# -------- FOOTER --------
st.markdown("---")
st.markdown(
    "Developed as an AI-based Smart City solution for predicting public transport crowd levels."
)
