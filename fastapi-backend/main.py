from fastapi import FastAPI, UploadFile, File
from api.router import api_router

app = FastAPI(title="Traffic Sign Recognition")

app.include_router(api_router)

