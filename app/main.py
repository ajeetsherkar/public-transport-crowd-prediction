from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="Public Transport Crowd Prediction API")

# -------- PATH HANDLING (IMPORTANT) --------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "crowd_model.pkl"
ENCODER_PATH = BASE_DIR / "models" / "label_encoders.pkl"

# -------- LOAD MODEL --------
model = joblib.load(MODEL_PATH)
label_encoders = joblib.load(ENCODER_PATH)


class CrowdRequest(BaseModel):
    route_id: str
    hour: int
    day_type: str
    is_holiday: int
    weather: str


@app.get("/")
def home():
    return {"message": "Crowd Prediction API is running"}


@app.post("/predict")
def predict_crowd(data: CrowdRequest):

    df = pd.DataFrame([{
        "route_id": data.route_id,
        "hour": data.hour,
        "day_type": data.day_type,
        "is_holiday": data.is_holiday,
        "weather": data.weather
    }])

    # Encode categorical inputs
    for col in ["route_id", "day_type", "weather"]:
        df[col] = label_encoders[col].transform(df[col])

    prediction = model.predict(df)[0]
    crowd_level = label_encoders["crowd_level"].inverse_transform([prediction])[0]

    return {"predicted_crowd_level": crowd_level}
