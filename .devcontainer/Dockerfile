FROM python:3.9-slim

# Add any additional system packages you need here
RUN apt-get update && apt-get install -y \
sqlite3

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
