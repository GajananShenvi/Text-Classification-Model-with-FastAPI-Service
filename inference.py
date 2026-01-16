#from cache import cached_predict
#def predict_text(text: str):
#    return cached_predict(text)


import torch
from model.text_model import TextClassifier

artifact_path = "model/artifacts.pth"

checkpoint = torch.load(artifact_path, map_location="cpu")

vectorizer = checkpoint["vectorizer"]
label_encoder = checkpoint["label_encoder"]

model = TextClassifier(
    input_dim=len(vectorizer.get_feature_names_out()),
    num_classes=len(label_encoder.classes_)
)

model.load_state_dict(checkpoint["model_state"])

device=torch.device("cpu")
model.to(device)
model.eval()

def predict_text(text: str):
    text=text.strip()

    X = vectorizer.transform([text]).toarray()
    X = torch.tensor(X, dtype=torch.float32).to(device)

    with torch.no_grad():
        outputs = model(X)
        pred = torch.argmax(outputs, dim=1).item()

    return label_encoder.inverse_transform([pred])[0]
