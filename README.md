# 🧠 Text Classification Model with FastAPI Service

A production-ready **Text Classification API** built using **PyTorch** and **FastAPI**.  
This project demonstrates how to train a text classification model and expose it as a RESTful service for real-time inference.

---

## 🚀 Project Overview

This repository contains:
- A trained **text classification model**
- A **FastAPI** backend to serve predictions
- Clean project structure suitable for interviews and real-world deployment

The API accepts raw text and returns the predicted category.

---

## ✨ Key Features

- ✅ Text classification using **PyTorch**
- ⚡ FastAPI for high-performance inference
- 📦 Model loading at startup for faster predictions
- 📄 Auto-generated API docs (Swagger UI)
- 🧪 Easy to test using Postman / curl / browser

---

## 📁 Project Structure

```
Text-Classification-Model-with-FastAPI-Service/
│
├── dataset/                # Dataset used for training
├── model/                  # Model architecture and helpers
├── __pycache__/            # Python cache files
│
├── artifacts.pth           # Trained PyTorch model weights
├── app.py                  # FastAPI application
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```


## Install Dependencies
pip install -r requirements.txt

## Run the FastAPI Server
uvicorn app:app --reload

Server will start at:  http://127.0.0.1:8000

## API Documentation (Swagger UI)

FastAPI provides interactive API documentation using Swagger UI.
Once the server is running, open the following URL in your browser to access and test all available endpoints:

http://127.0.0.1:8000/docs



