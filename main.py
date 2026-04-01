from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI(title="Real Estate Predictor API")


model = joblib.load('house_model.pkl')



class HouseFeatures(BaseModel):
    bedrooms: int
    sq_ft: float
    age: int


@app.get("/")
def health_check():
    return {"status": "healthy", "message": "This is testing"}


@app.post("/predict")
def predict_price(features: HouseFeatures):

    input_data = [[features.bedrooms, features.sq_ft, features.age]]
    prediction = model.predict(input_data)
    return {
        "predicted_price": round(prediction[0], 2),
        "currency": "USD"
    }