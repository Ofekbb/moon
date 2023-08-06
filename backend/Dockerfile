FROM python:3.8-slim

WORKDIR /app

# Copy the Flask app to the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port
EXPOSE 5001

CMD ["python", "backend.py"]
