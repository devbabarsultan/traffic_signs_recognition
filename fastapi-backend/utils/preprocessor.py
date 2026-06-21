import cv2 as cv
import numpy as np
import io
from PIL import Image 

image_dimensions = (32, 32, 3)

def preprocess_image(content):

    pil_image = Image.open(io.BytesIO(content))
    image_array = np.array(pil_image)
    img = cv.cvtColor(image_array, cv.COLOR_RGB2BGR)

    img = cv.resize(img, (image_dimensions[0], image_dimensions[1]))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
    img = cv.equalizeHist(img) 
    
    img = img / 255.0
    img = img.reshape(1, image_dimensions[0], image_dimensions[1], 1).astype(np.float32) 
    
    return img