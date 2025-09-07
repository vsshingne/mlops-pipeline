import io
import random
import time
from typing import Optional, List, Tuple

from PIL import Image

class DummyModel:
    def __init__(self, version: str = "v0-dummy"):
        self.version = version
        self.labels = ["cat", "dog", "car", "garbage", "unknown"]

    def _predict_label(self) -> str:
        return random.choice(self.labels)

    def _confidence(self) -> float:
        return round(random.uniform(0.70, 0.99), 2)

    def predict_image_bytes(self, data: bytes) -> Tuple[str, float]:
        # Validate that the file is a readable image
        try:
            Image.open(io.BytesIO(data)).verify()
        except Exception:
            # If it's not a valid image, return an error label
            return "invalid_image", 0.0
        
        # If valid, return a random prediction
        return self._predict_label(), self._confidence()

    def predict_features(self, feats: List[float]) -> Tuple[str, float]:
        # Simple rule for feature-based prediction
        if int(sum(feats)) % 2 == 0:
            label = "even-class"
        else:
            label = "odd-class"
        return label, self._confidence()

# --- Singleton Pattern for Model Loading ---
# This ensures the model is created only once.
model: Optional[DummyModel] = None

def load_model() -> DummyModel:
    """Loads the dummy model into a singleton instance."""
    global model
    if model is None:
        model = DummyModel()
    return model

def timed(fn, *args, **kwargs):
    """A helper function to time the execution of another function."""
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return out, (t1 - t0) * 1000.0  # Return latency in milliseconds