from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("covid_diag.pkl")

app = FastAPI()

class PatientData(BaseModel):
    Age: int
    Gender: int
    Fever: int
    Cough: int
    Fatigue: int
    Breathlessness: int
    Comorbidity: int
    Stage: int
    Type: int
    Tumor_Size: float

@app.get("/")
def welcome():
    return {"message": "Welcome to COVID Survival Rate Predictor API"}

@app.post("/predict")
def predict_survival(data: PatientData):
    features = np.array([[
        data.Age, data.Gender, data.Fever, data.Cough, data.Fatigue,
        data.Breathlessness, data.Comorbidity, data.Stage,
        data.Type, data.Tumor_Size
    ]])

    prediction = model.predict(features)
    return {"predicted_survival_rate": round(prediction[0], 2)}
