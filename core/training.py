from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam
from core.config import Config

def train_model(data_path="data/", model_save_path=Config.MODEL_PATH):
    datagen = ImageDataGenerator(rescale=1.0/255, validation_split=0.2)

    train_gen = datagen.flow_from_directory(
        data_path, target_size=Config.IMAGE_SIZE, batch_size=32, class_mode="categorical", subset="training"
    )
    val_gen = datagen.flow_from_directory(
        data_path, target_size=Config.IMAGE_SIZE, batch_size=32, class_mode="categorical", subset="validation"
    )

    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(len(Config.CLASSES), activation='softmax'),
    ])

    model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(train_gen, validation_data=val_gen, epochs=10)
    model.save(model_save_path)
    print(f"Model saved to {model_save_path}")


if __name__ == "__main__":
    # Call the train_model function when the script is executed
    train_model()


