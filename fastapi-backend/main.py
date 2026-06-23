from fastapi import FastAPI, UploadFile, File
from  contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

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
origins = ["https://trafic-sign-recognition-devbabarsultan.streamlit.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          
    allow_credentials=True,         
    allow_methods=["*"],            
    allow_headers=["*"],            
)

app.include_router(api_router)

