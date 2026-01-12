from locust import HttpUser, task, between
import pandas as pd
import random

# Load dataset once (important for performance)
df = pd.read_csv("'../dataset/extended_amazon_products.csv'")

texts = df["text"].dropna().tolist()

class TextClassificationUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def predict_from_dataset(self):
        sample_text = random.choice(texts)

        self.client.post(
            "/predict",
            json={"text": sample_text}
        )
