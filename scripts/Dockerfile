FROM python:3.8

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install wamerican && \
    pip install --no-cache-dir -r requirements.txt \
    pip install --no-binary lxml lxml

COPY *.py ./
