import io
import random
import time
from typing import Optional, List, Tuple

from PIL import Image

class DummyModel:
    """A simple dummy model for placeholder predictions."""
    def __init__(self, version: str = "v1.0.0-dummy"):
        self.version = version
        self.labels = ["cat", "dog", "car", "person", "tree"]

    def _predict_label(self) -> str:
        """Returns a random prediction label."""
        return random.choice(self.labels)

    def _confidence(self) -> float:
        """Returns a random confidence score."""
        return round(random.uniform(0.70, 0.99), 2)

    def predict_image_bytes(self, data: bytes) -> Tuple[str, float]:
        """
        Validates that the input is an image and returns a random prediction.
        """
        try:
            # Use Pillow to verify that the file is a valid image
            Image.open(io.BytesIO(data)).verify()
        except Exception:
            # If it's not a valid image, return an error label
            return "invalid_image", 0.0
        
        # If valid, return a random prediction
        return self._predict_label(), self._confidence()

    def predict_features(self, feats: List[float]) -> Tuple[str, float]:
        """
        Returns a prediction based on a simple rule for a list of features.
        """
        if int(sum(feats)) % 2 == 0:
            label = "even-class"
        else:
            label = "odd-class"
        return label, self._confidence()

# --- Singleton Pattern for Model Loading ---
# This ensures the model is created only once during the application's life.
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