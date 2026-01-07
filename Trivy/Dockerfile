# VULNERABILITY: Outdated base image (Debian Buster is old)
FROM python:3.7-slim-buster

WORKDIR /app

# VULNERABILITY: Running as root (default behavior)
# No USER defined
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]