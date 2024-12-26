from fastapi import APIRouter, UploadFile, File
from core.prediction import predict_image
from api.schemas import PredictionResponse

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Preprocess and predict
    result = predict_image(file.file)
    return {"file": file.filename, "result": result}
