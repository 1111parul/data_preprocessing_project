# # Use a Python base image
# FROM python:3.8-slim

# # Set working directory
# WORKDIR /app

# # Copy project files
# COPY requirements.txt .
# COPY src/ ./src/
# COPY README.md .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Command to run the application (modify as needed)
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8082"]



# Use a Python base image
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app
COPY . /app

# # Copy dependency file
# COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-multipart


# Copy the rest of the application
COPY api/main.py .
COPY Readme.md .

# Expose port 8082 for external access
EXPOSE 8082

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8082"]

