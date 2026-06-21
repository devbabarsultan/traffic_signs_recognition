import cv2 as cv

image_dimensions = (32, 32, 3)

def preprocess_image(image):

    img = cv.imread(image)
    if img is None:
        raise ValueError(f"Image not found.")

    img = cv.resize(img, (image_dimensions[0], image_dimensions[1]))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
    img = cv.equalizeHist(img) 
    img = img / 255.0
    img = img.reshape(1, image_dimensions[0], image_dimensions[1], 1) 
    
    return img