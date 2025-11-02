# ML Service Dockerfile
FROM python:3.10-slim

WORKDIR /ml_service

COPY ./ml_service /ml_service

RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn

EXPOSE 8001

CMD ["uvicorn", "api.ml_api:app", "--host", "0.0.0.0", "--port", "8001"]
