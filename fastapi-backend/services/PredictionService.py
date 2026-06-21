import numpy as np
import pandas as pd

from utils.preprocessor import preprocess_image
from core.config import settings


def predict_image(image,session,input_name):

    processed_image = preprocess_image(image)

    outputs = session.run(None, {input_name: processed_image})

    # Get prediction
    predictions = outputs[0]

    class_id = int(np.argmax(predictions))
    labels = pd.read_csv(settings.LABELS_PATH)
    predicted_class = labels.iloc[class_id,1]

    confidence = float(np.max(predictions))

   
    return predicted_class, confidence
