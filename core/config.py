import os

# Define all configuration variables
class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "models/cat_dog_model.h5")
    IMAGE_SIZE = (128, 128)  # Input image size
    CLASSES = ["cat", "dog"]
