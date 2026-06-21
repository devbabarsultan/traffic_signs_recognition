from fastapi import FastAPI, APIRouter, UploadFile, File
from services.get_prediction import predict_image
import io
from PIL import Image


router = APIRouter()

@router.post("/predict")
def predict(file: UploadFile = File(...)):

    image_bytes = file.read()
    image = Image.open(io.BytesIO(image_bytes))

    prediction = predict_image(image)

    return prediction

    