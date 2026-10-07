# Use official Python 3.12 slim image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (for Docker layer caching)
COPY requirements.txt .

# Install dependencies — no venv needed inside Docker
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY main.py .

# Expose port 8000 so Docker knows the app listens on it
EXPOSE 8000

# Start the application using Uvicorn
# 0.0.0.0 makes it accessible from outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
