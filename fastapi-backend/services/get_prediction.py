import numpy as np

from model.model_loader import load_model
from services.preprocessor import preprocess_image
from core.config import settings

session, input_name = load_model(settings.MODEL_PATH)

def predict_image(model, image):

    processed_image = preprocess_image(image)

    outputs = session.run(None, {input_name: image})

    # Get prediction
    predictions = outputs[0]
    class_id = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    return class_id, confidence
