# Lightweight base
FROM python:3.10-slim

# System packages (Pillow works without extra libs; keep lean)
WORKDIR /app

# Leverage layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY ./app .

# Expose FastAPI port
EXPOSE 8000

# Uvicorn entry
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
# CMD ["sleep", "infinity"]