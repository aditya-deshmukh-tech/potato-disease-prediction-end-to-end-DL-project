import logging
import tensorflow as tf
from tensorflow.keras.models import load_model
from app.core.config import PROJECT_ROOT

model = None

MODEL_PATH = PROJECT_ROOT / "DL_Models" / "potato_disease_cnn.keras"
logger = logging.getLogger(__name__)

def load_DL_model():
    global model

    if model is None:
        with open(MODEL_PATH, "rb") as f:
            logger.info("loading DL model....")
            logger.info(f"tensorflow version : {tf.__version__}")
            model = load_model(MODEL_PATH)
    return model


def get_model():
    if model is None:
        load_DL_model()
    return model
