import onnxruntime as ort
from core.config import settings

def load_model(model_path: str):

    session = ort.InferenceSession(settings.MODEL_PATH)
    input_name = session.get_inputs()[0].name
    
    return session, input_name