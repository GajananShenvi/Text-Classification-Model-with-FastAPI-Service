from functools import lru_cache
from model import predict

@lru_cache(maxsize=256)
def cached_predict(text):
    return predict(text)
