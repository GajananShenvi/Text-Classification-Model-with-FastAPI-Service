# Text Classification Model with FastAPI Service 🚀

A RESTful text classification API built with **FastAPI** that serves a trained machine learning model to perform text classification tasks. This project includes Docker support for easy deployment and scaling.

---

## 🧠 Project Overview

This repository implements a text classification system using a pre-trained model wrapped inside a FastAPI application. The API exposes inference endpoints that allow users to send text and receive predicted class labels in JSON format.

Key features:
- Fast and scalable API using FastAPI
- Modular code structure with inference, caching, and logging
- Docker + Docker-Compose setup for easy deployment
- Model loading and prediction logic separated for clarity

---

## 📁 Repository Structure

```text
.
├── model/                      # Trained model files
├── performance/                # Performance results / plots (if any)
├── Docker_File/                # Docker config files (Dockerfile, etc.)
├── app.py                     # Main FastAPI application
├── inference.py               # Model inference logic
├── cache.py                   # Caching utilities
├── logger.py                  # Logger setup
├── docker-compose.yml         # Docker-Compose configuration
├── requirement.txt            # Python dependencies
└── README.md                  # This file
```

## 📦 Requirements

Before running the project locally, make sure you have:

-Python 3.8+
-Pip package manager
-(Optional for Docker) Docker & Docker-Compose

Install dependencies:  
pip install -r requirement.txt

## 🚀 Run Locally

Start the FastAPI server locally:
uvicorn app:app --reload

By default, your API will run at:
http://127.0.0.1:8000

You can access automatic API docs at:
http://127.0.0.1:8000/docs


## 🐳 Docker Deployment

Build and run the project using Docker:
docker build -t text-classification-fastapi .
docker run -p 8000:8000 text-classification-fastapi


Or using docker-compose:
docker-compose up --build

## 🛠️ Code Highlights
#inference.py

Contains logic to:

-Load the saved model
-Preprocess incoming requests
-Run predictions

## cache.py
Utility to cache repeated predictions and speed up responses (if enabled).

## logger.py
Central logging setup used throughout the app.

## 🤖 Model

Your trained text classification model is stored and loaded from the model/ folder. This can be updated over time with improved models. The API automatically uses whatever model files are in that folder.

## 📈 Performance

If you have evaluation reports, plots, or logs in the performance/ directory, they can help explain how the model performs on test data.




