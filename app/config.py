import os
from dataclasses import dataclass

@dataclass
class Settings:
    MODEL_PATH: str = os.getenv("MODEL_PATH", "models/best.pt")  # placeholder for later
    APP_NAME: str = os.getenv("APP_NAME", "ml-pipeline")
    VERSION: str = os.getenv("VERSION", "0.1.0")

settings = Settings()
