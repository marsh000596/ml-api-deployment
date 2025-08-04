# app/model.py

import joblib
import os
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")

def load_model():
    return joblib.load(model_path)

def predict(model, features: np.ndarray) -> int:
    # Ensure features is 2D array
    if features.ndim == 1:
        features = features.reshape(1, -1)

    prediction = model.predict(features)
    return int(prediction[0])
