import os
import random
import numpy as np
import tensorflow as tf
from fastapi import UploadFile, File, HTTPException
from .model_store import get_model
from ..core.config import PROJECT_ROOT

allowed_content_type = {"png", "jpg", "jpeg"}

class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

def upload_image(image: UploadFile = File(...)):
    content_type = image.content_type.split("/")[1]
    content_type = content_type.lower()
    if content_type not in allowed_content_type:
        raise HTTPException(status_code=400, detail="Unsupported content type")
    file_name = f"image-{random.randrange(1000, 9999)}.{content_type}"
    file_path = os.path.join(PROJECT_ROOT / "uploads", file_name)

    with open(file_path, "wb+") as f:
        f.write(image.file.read())
        f.close()

    return file_name, file_path

async def predict_potato_disease(image: UploadFile = File(...)):
    img_name, img_path = upload_image(image)
    img = tf.keras.utils.load_img(img_path)
    img_arr = tf.keras.preprocessing.image.img_to_array(img)
    img_arr = np.expand_dims(img_arr, axis=0)
    model = get_model()
    predictions = model.predict(img_arr)
    return {"prediction" : class_names[np.argmax(predictions[0])], "image" : f"http://localhost:8080/api/v1/image/{img_name}"}

async def preview_potato_image(image_name: str):
    file_path = os.path.join(PROJECT_ROOT / "uploads", image_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="file not present")

    return {"file_path": file_path, "file_name": image_name, "media_type": f"image/{image_name.split(".")[1]}"}