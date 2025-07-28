# Use official Python slim image with AMD64 platform
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY . .

# Make the main script executable
RUN chmod +x round1b_main.py

# Run the Round 1B solution
CMD ["python3", "round1b_main.py"]
