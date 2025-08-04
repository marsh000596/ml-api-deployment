# app/utils.py
import numpy as np
from app.schemas import PredictionRequest

def preprocess(request: PredictionRequest) -> np.ndarray:
    return np.array([[request.feature1, request.feature2]])  # shape = (1, 2)
