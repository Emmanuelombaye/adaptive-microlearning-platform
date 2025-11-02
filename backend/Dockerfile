# Backend Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY ./backend /app

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pymysql passlib python-dotenv

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
