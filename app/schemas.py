from pydantic import BaseModel, Field
from typing import List, Optional

class JsonInferenceRequest(BaseModel):
    features: List[float] = Field(..., description="Numeric features for dummy model")

class InferenceResponse(BaseModel):
    filename: Optional[str] = None
    prediction: str
    confidence: float
    latency_ms: float
    model_version: str
