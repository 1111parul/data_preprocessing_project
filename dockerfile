# Use a Python base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY src/ ./src/
COPY README.md .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the application (modify as needed)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
