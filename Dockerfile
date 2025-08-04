FROM python:3.11-slim

# Avoid interactive prompts during package installs
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install OS-level dependencies (only what's needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements to leverage Docker caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY ./app ./app

# Expose port for Uvicorn
EXPOSE 8000

# Run the API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
