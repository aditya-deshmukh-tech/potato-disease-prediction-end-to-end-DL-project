from fastapi import FastAPI
from app.api import health, potato_disease_api, potato_disease_ui
from app.core.config import create_upload_dir_if_not_exist
from app.core.logging_config import setup_logging
from app.services.model_store import load_DL_model

setup_logging()

app = FastAPI()

@app.on_event("startup")
def load_model():
    load_DL_model()
    create_upload_dir_if_not_exist()


app.include_router(health.router, prefix="/api")
app.include_router(potato_disease_api.router, prefix="/api/v1")
app.include_router(potato_disease_ui.router, prefix="/ui")
        