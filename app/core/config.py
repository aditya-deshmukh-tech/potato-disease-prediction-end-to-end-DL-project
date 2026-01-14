import os
from pathlib import Path
from pydantic import Field
from pydantic_settings import BaseSettings

PROJECT_ROOT = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_name: str = Field("My FastAPI App", env="APP_NAME")
    log_level: str = Field("INFO", env="LOG_LEVEL")

    class Config:
        env_file = ".env"

settings = Settings()


def create_upload_dir_if_not_exist():
    file_upload_dir = PROJECT_ROOT / "uploads"
    if not os.path.exists(file_upload_dir):
        os.makedirs(file_upload_dir)