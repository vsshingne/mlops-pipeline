# ML Deployment Pipeline (Phase 1 - Local + Docker)

This is a minimal FastAPI service you will later connect to CI/CD and AWS.
It supports **either** image upload or JSON features on `/infer`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
