from fastapi import FastAPI, APIRouter, UploadFile, File

router = APIRouter()

@router.post("/predict")
def predict(file: UploadFile = File(...)):

    image_bytes = file.read()
    print(f"Received file: {file.filename}")
    # Here you would add your prediction logic using the uploaded file
    return {"filename": file.filename, "prediction": "dummy_prediction",
            "file_size": len(image_bytes), "content_type": file.content_type}