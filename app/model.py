import time
from typing import Optional, List, Tuple
from sklearn.tree import DecisionTreeClassifier
import numpy as np

class SklearnModel:
    def __init__(self):
        self.model = DecisionTreeClassifier()
        self.version = "sklearn-test-v1"
        # In a real scenario, you'd fit the model: self.model.fit(X, y)

    def predict_features(self, feats: List[float]) -> Tuple[str, float]:
        # Simple dummy prediction logic
        if np.sum(feats) > 10.0:
            return "high-value", 0.95
        return "low-value", 0.85

model_instance: Optional[SklearnModel] = None

def load_model() -> SklearnModel:
    global model_instance
    if model_instance is None:
        model_instance = SklearnModel()
    return model_instance

def timed(fn, *args, **kwargs):
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return out, (t1 - t0) * 1000.0