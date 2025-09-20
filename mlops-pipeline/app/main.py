from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from schemas import JsonInferenceRequest, InferenceResponse
from model import load_model, timed

app = FastAPI(title=settings.APP_NAME, version=settings.VERSION)

# CORS (handy if you add a frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the MLOps Template API!",
        "documentation": "Go to the /docs endpoint to see the interactive API."
    }

@app.get("/healthz")
async def health_check():
    return {"status": "ok", "service": settings.APP_NAME, "version": settings.VERSION}


# --------------------
# IMAGE INFERENCE
# --------------------
@app.post("/infer_file", response_model=InferenceResponse)
async def infer_file(file: UploadFile = File(..., description="Upload an image file")):
    mdl = load_model()
    data = await file.read()
    (pred, conf), latency = timed(mdl.predict_image_bytes, data)
    return InferenceResponse(
        filename=file.filename,
        prediction=pred,
        confidence=conf,
        latency_ms=round(latency, 2),
        model_version=mdl.version,
    )


# --------------------
# JSON INFERENCE
# --------------------
@app.post("/infer_json", response_model=InferenceResponse)
async def infer_json(json_body: JsonInferenceRequest = Body(..., description="JSON with features")):
    mdl = load_model()
    (pred, conf), latency = timed(mdl.predict_features, json_body.features)
    return InferenceResponse(
        filename=None,
        prediction=pred,
        confidence=conf,
        latency_ms=round(latency, 2),
        model_version=mdl.version,
    )
