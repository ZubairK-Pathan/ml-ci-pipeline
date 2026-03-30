from fastapi import FastAPI
from pydantic import BaseModel
import joblib


app = FastAPI(title="Real Estate Predictor API")


model = joblib.load('house_model.pkl')


# Define the expected JSON input format
class HouseFeatures(BaseModel):
    bedrooms: int
    sq_ft: float
    age: int


@app.get("/")
def health_check():
    return {"status": "healthy", "message": "API is running!"}


@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Format the incoming JSON data for the model
    input_data = [[features.bedrooms, features.sq_ft, features.age]]

    # Generate the prediction
    prediction = model.predict(input_data)

    return {
        "predicted_price": round(prediction[0], 2),
        "currency": "USD"
    }