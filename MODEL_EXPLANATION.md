# Model Explanation & Evaluation

---

## 1. Why PyTorch?

I used PyTorch because the project required building a **custom text classification model** and serving it through an API. PyTorch made it easy to define the model (`text_model.py`), load trained weights (`artifacts.pth`), and reuse the same model during inference in FastAPI. It also allowed better debugging and control compared to higher-level libraries.

---

## 2. What model did you use?

I used a **simple neural network–based text classification model**.
Text is first converted into numerical features, which are passed through a feed-forward neural network to predict the class. The model is intentionally simple to keep training, inference, and deployment stable.

---

## 3. Why is this model suitable for your project?

This model is suitable because:

* The dataset is structured and category-based
* The model is lightweight and fast for API inference
* It avoids unnecessary complexity
* It integrates cleanly with FastAPI

For this project, reliability and simplicity were more important than using a heavy model like BERT.

---

## 4. How did you evaluate the model?

* Tracked training loss, accuracy, recall, precession and F1-score
* Stored evaluation results in `metrics.json`
* Tested predictions using the FastAPI `/predict` endpoint
* Performed load testing using Locust to check API stability

This ensured both **model correctness** and **service performance**.

---

## 5. How good is the model?

The model performs well for basic text classification tasks and responds quickly during inference.
However, it has limitations in understanding deep context and semantics. Overall, it is **appropriate for the project scope and demonstrates correct ML-to-API deployment workflow**.

---
