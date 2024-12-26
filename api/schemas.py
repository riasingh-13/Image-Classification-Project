from pydantic import BaseModel

class PredictionResponse(BaseModel):
    file: str
    result: dict
