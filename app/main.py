# app/main.py

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.schemas import PredictionRequest, PredictionResponse
from app.model import load_model, predict
from app.utils import preprocess
import traceback

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
model = load_model()

# -------------------------------
# 1. Home Page
# -------------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# ---------------------------------------
# 2. Web Form Submission
# ---------------------------------------
@app.post("/predict_web", response_class=HTMLResponse)
async def predict_web(request: Request,
                      feature1: float = Form(...),
                      feature2: float = Form(...)):

    try:
        # Prepare input dictionary
        data = {
            "feature1": feature1,
            "feature2": feature2,
        }

        features = preprocess(PredictionRequest(**data))
        prediction = predict(model, features)

        return templates.TemplateResponse("home.html", {
            "request": request,
            "prediction": prediction
        })

    except Exception as e:
        print("🔥 Internal Server Error:\n", traceback.format_exc())
        return templates.TemplateResponse("home.html", {
            "request": request,
            "error": f"Internal Server Error: {str(e)}"
        })


# ---------------------------------------
# 3. JSON API Endpoint
# ---------------------------------------
@app.post("/predict_web", response_class=HTMLResponse)
async def predict_web(request: Request,
                      feature1: float = Form(...),
                      feature2: float = Form(...)):

    try:
        # Prepare input dictionary
        data = {
            "feature1": feature1,
            "feature2": feature2,
        }

        features = preprocess(PredictionRequest(**data))
        prediction = predict(model, features)

        print("Prediction:", prediction)  # ✅ Good to keep for debugging

        return templates.TemplateResponse("home.html", {
            "request": request,
            "prediction": prediction
        })

    except Exception as e:
        print("🔥 Internal Server Error:\n", traceback.format_exc())
        return templates.TemplateResponse("home.html", {
            "request": request,
            "error": f"Internal Server Error: {str(e)}"
        })
