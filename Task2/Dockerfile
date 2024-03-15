FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY . .

ENTRYPOINT ["/bin/bash", "-c", "python app.py"]
