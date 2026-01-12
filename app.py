from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
from functools import lru_cache

from model.text_model import TextClassifier

app = FastAPI(title="Text Classification API")

# Load trained artifacts
checkpoint = torch.load("model/artifacts.pth", map_location="cpu")

vectorizer = checkpoint["vectorizer"]
label_encoder = checkpoint["label_encoder"]

model = TextClassifier(
    input_dim=len(vectorizer.get_feature_names_out()),
    num_classes=len(label_encoder.classes_)
)

model.load_state_dict(checkpoint["model_state"])
model.eval()

# Request schema

class TextRequest(BaseModel):
    text: str

# Caching
@lru_cache(maxsize=256)
def cached_predict(text: str):
    vector = vectorizer.transform([text]).toarray()
    vector = torch.tensor(vector, dtype=torch.float32)

    with torch.no_grad():
        outputs = model(vector)
        prediction = torch.argmax(outputs, dim=1).item()

    return label_encoder.inverse_transform([prediction])[0]

# API Endpoint
@app.post("/predict")
def predict(request: TextRequest):
    text = request.text.strip()

    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    try:
        category = cached_predict(text)
        return {"predicted_category": category}
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")
