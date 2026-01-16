# Text Classification Model with FastAPI Service

A **Text Classification REST API** built using **PyTorch** and **FastAPI**.
This project demonstrates how to train a text classification model and expose it as a scalable web service.

The API accepts raw text as input and returns the predicted class label.
This project is designed to be **simple, beginner-friendly**, and suitable for **interviews, learning, and deployment**.

---

## 🚀 Features

* 🧠 Text classification using **PyTorch**
* ⚡ High-performance REST API with **FastAPI**
* 📦 Model inference via API endpoint
* 📊 Easy to test using Swagger UI
* 🐳 Docker support for deployment
* 🧪 Load testing support using **Locust**

---

## 🏗️ Project Structure

```
Text-Classification-Model-with-FastAPI-Service/
│
├── __pycache__/                     # Python bytecode cache
│
├── dataset/
│   └── extended_amazon_pro...csv    # Dataset used for training/testing
│
├── model/
│   ├── __pycache__/                 # Model-related cache files
│   ├── text_model.py                # PyTorch model architecture
│   ├── artifacts.pth                # Trained model weights
│   ├── metrics.json                 # Model evaluation metrics
│   └── train.ipynb                  # Model training notebook
│
├── performance/
│   └── locustfile.py                # Load testing using Locust
│
├── app.py                           # FastAPI application entry point
├── inference.py                     # Model loading & inference logic
├── cache.py                         # Caching logic for predictions
├── logger.py                        # Logging configuration
│
├── Docker_File                      # Docker configuration file
├── docker-compose.yml               # Docker Compose configuration
│
├── README.md                        # Project documentation
├── requirement.txt                  # Python dependencies

```

---

## 🛠️ Tech Stack

* **Python**
* **PyTorch**
* **FastAPI**
* **Uvicorn**
* **Docker**
* **Locust**

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/GajananShenvi/Text-Classification-Model-with-FastAPI-Service.git
cd Text-Classification-Model-with-FastAPI-Service
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI provides built-in interactive documentation:

* **Swagger UI** → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc** → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔍 API Usage Example

### Endpoint

```
POST /predict
```

### Request Body

```json
{
  "text": "This product is really amazing"
}
```

### Response

```json
{
  "prediction": "positive"
}
```

---

## 🧠 Model Details

* The model is trained using **PyTorch**
* Text data is preprocessed and converted into numerical features
* The trained model is saved as `artifacts.pth`
* Model is loaded once at API startup for efficient inference

---

## 🐳 Docker Usage

### Build Docker Image

```bash
docker build -t text-classifier-api .
```

### Run Container

```bash
docker run -p 8000:8000 text-classifier-api
```

---

## 📈 Load Testing (Locust)

To test performance under load:

```bash
locust -f performance/locustfile.py
```

Then open:

```
http://localhost:8089
```

