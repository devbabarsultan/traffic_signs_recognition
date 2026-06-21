import onnxruntime as ort
from core.config import settings

def load_model(model_path: str = settings.MODEL_PATH):

    session = ort.InferenceSession(model_path)
    input_name = session.get_inputs()[0].name
    
    return session, input_name