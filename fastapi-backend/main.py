from fastapi import FastAPI, UploadFile, File
from  contextlib import asynccontextmanager

from api.router import api_router
from services.ModelService import load_model
from core.config import settings

@asynccontextmanager
async def lifespan(app:FastAPI):

    print("----------------Loading Model--------------")
    session, input_name = load_model(settings.MODEL_PATH)

    app.state.model_session = session
    app.state.model_input_name = input_name

    yield
 

app = FastAPI(
            title="Traffic Sign Recognition",
            description="API for traffic sign recognition using ONNX model",
            version="1.0.0",
            lifespan=lifespan
            )

app.include_router(api_router)

