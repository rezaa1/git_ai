FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Set GITHUB_TOKEN environment variable
ENV GITHUB_TOKEN=your_github_token_here

# Command to run the application
CMD ["python", "-m", "app"]
