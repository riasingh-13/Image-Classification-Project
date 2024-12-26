import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from core.config import Config

model = load_model(Config.MODEL_PATH)

def preprocess_image(image):
    img = Image.open(image)
    img = img.resize(Config.IMAGE_SIZE)
    return np.expand_dims(np.array(img) / 255.0, axis=0)

def predict_image(image):
    processed_image = preprocess_image(image)
    predictions = model.predict(processed_image)
    class_idx = np.argmax(predictions)
    confidence = float(predictions[0][class_idx])
    return {"prediction": Config.CLASSES[class_idx], "confidence": confidence}
