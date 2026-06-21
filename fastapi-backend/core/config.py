from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    PROJECT_NAME: str = "Traffic Detection API"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    MODEL_PATH: str = "artifacts/traffic_sign_model.onnx"
    LABELS_PATH: str = "artifacts/labels.csv"


settings = Settings()