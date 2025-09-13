import os
import io
import time
from typing import Optional, List, Tuple

from PIL import Image
from ultralytics import YOLO
from google.cloud import storage

# --- Configuration ---
# ❗️ UPDATE THESE TWO LINES WITH YOUR DETAILS \\
GCS_BUCKET_NAME = "your-unique-bucket-name"
MODEL_FILE_KEY = "best.pt"
# -----------------------------------------

LOCAL_MODEL_PATH = f"/tmp/{MODEL_FILE_KEY}"

class RealModel:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)
        self.version = model_path

    def predict_image_bytes(self, image_bytes: bytes) -> Tuple[str, float]:
        try:
            image = Image.open(io.BytesIO(image_bytes))
            results = self.model(image)

            if not results or not results[0].boxes:
                return "no_detection", 0.0

            top_result = results[0].boxes[0]
            top_conf = float(top_result.conf[0])
            top_cls_index = int(top_result.cls[0])
            top_cls_name = self.model.names[top_cls_index]

            return top_cls_name, round(top_conf, 4)
        except Exception as e:
            print(f"Error processing image: {e}")
            return "invalid_image", 0.0

model_instance: Optional[RealModel] = None

def load_model() -> RealModel:
    global model_instance
    if model_instance is None:
        if not os.path.exists(LOCAL_MODEL_PATH):
            print(f"Downloading model from gs://{GCS_BUCKET_NAME}/{MODEL_FILE_KEY}...")
            client = storage.Client()
            bucket = client.bucket(GCS_BUCKET_NAME)
            blob = bucket.blob(MODEL_FILE_KEY)
            os.makedirs(os.path.dirname(LOCAL_MODEL_PATH), exist_ok=True)
            blob.download_to_filename(LOCAL_MODEL_PATH)
            print("Model downloaded successfully.")

        print(f"Loading model from {LOCAL_MODEL_PATH}...")
        model_instance = RealModel(LOCAL_MODEL_PATH)
        print("Model loaded successfully.")

    return model_instance

def timed(fn, *args, **kwargs):
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return out, (t1 - t0) * 1000.0