from functools import lru_cache
from model import predict

@lru_cache(maxsize=128)
def cached_predict(text):
    return predict(text)
