from model.model_loader import load_model
from services.preprocessor import preprocess_image
from core.config import settings

model = load_model(settings.MODEL_PATH)

def predict_image(model, image):

    processed_image = preprocess_image(image)

    prediction = model.predict()

    return prediction
