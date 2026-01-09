from fastapi import FastAPI
import torch
import numpy as np
from model.text_model import TextClassifier


app = FastAPI()

# Load artifacts
checkpoint = torch.load("model/artifacts.pth", map_location="cpu")

vectorizer = checkpoint["vectorizer"]
label_encoder = checkpoint["label_encoder"]

model = TextClassifier(
    input_dim=len(vectorizer.get_feature_names_out()),
    num_classes=len(label_encoder.classes_)
)
model.load_state_dict(checkpoint["model_state"])
model.eval()

@app.post("/predict")
def predict(text: str):
    vector = vectorizer.transform([text]).toarray()
    vector = torch.tensor(vector, dtype=torch.float32)

    with torch.no_grad():
        outputs = model(vector)
        prediction = torch.argmax(outputs, dim=1).item()

    category = label_encoder.inverse_transform([prediction])[0]
    return {"predicted_category": category}

