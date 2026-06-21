from fastapi import FastAPI, APIRouter, UploadFile, File, Request
from services.PredictionService import predict_image
import numpy as np
import cv2 as cv


router = APIRouter()

@router.post("/predict")
async def predict(request: Request, file: UploadFile = File(...)):

    content = await file.read()

    
    session = request.app.state.model_session
    input_name = request.app.state.model_input_name


    predicted_class, confidence = predict_image(content, session, input_name)

    return {"Prediction": predicted_class,
            "Score": confidence,
            "status": "200"
            }

    