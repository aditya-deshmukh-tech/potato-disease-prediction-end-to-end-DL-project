from fastapi import APIRouter, UploadFile, File
import logging
from starlette.responses import FileResponse

from app.services.potato_disease_service import predict_potato_disease, preview_potato_image

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/predict_potato_disease")
async def predict(image: UploadFile = File(...)):
    return await predict_potato_disease(image)

@router.get("/image/{image_name}")
async def preview_image(image_name: str):
    image = await preview_potato_image(image_name)
    return FileResponse(path=image["file_path"], filename=image["file_name"],
                        media_type=image["media_type"])