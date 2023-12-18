FROM python:3.8-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi==0.68.0 uvicorn==0.15.0

# Expose port 8000
EXPOSE 8000

# Start the FastAPI app on port 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
