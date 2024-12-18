FROM python:3.9-slim

# Install dependencies
RUN apt-get update && apt-get install -y git
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy the project
WORKDIR /app
COPY src /app/src
COPY data /app/data

# Set the entry point
CMD ["python", "/app/src/main.py"]
