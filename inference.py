#from cache import cached_predict
#def predict_text(text: str):
#    return cached_predict(text)


import torch
from model.text_model import TextClassifier

checkpoint = torch.load("artifacts/artifacts.pth", map_location="cpu")

vectorizer = checkpoint["vectorizer"]
label_encoder = checkpoint["label_encoder"]

model = TextClassifier(
    input_dim=len(vectorizer.get_feature_names_out()),
    num_classes=len(label_encoder.classes_)
)

model.load_state_dict(checkpoint["model_state"])
model.eval()

def predict_text(text: str):
    X = vectorizer.transform([text]).toarray()
    X = torch.tensor(X, dtype=torch.float32)

    with torch.no_grad():
        outputs = model(X)
        pred = torch.argmax(outputs, dim=1)

    return label_encoder.inverse_transform(pred.numpy())[0]
