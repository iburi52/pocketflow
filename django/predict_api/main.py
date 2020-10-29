import keras
import numpy as np
from PIL import Image
from tensorflow.keras import backend as backend
from django.conf import settings


def predict(upload_image):
    result = []

    model_file_path = settings.MODEL_FILE_PATH
    model = keras.models.load_model(model_file_path)

    raw_image_open = Image.open(upload_image)
    raw_image_rgb = raw_image_open.convert("RGB")
    raw_image_resized = raw_image_rgb.resize((224, 224))

    np_data = np.asarray(raw_image_resized)
    norm_data = np_data / 255.0

    image_data = np.expand_dims(norm_data, axis=0)
    predicted_result = model.predict(image_data)
    result_coment = f"Dog:{predicted_result[0][0]*100:.1f}% / Cat:{predicted_result[0][1]*100:.1f}%"
    result.append(result_coment)

    backend.clear_session()

    return (result)










