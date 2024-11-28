FROM python:3.9-slim

WORKDIR /app

# Copy the application code
COPY app.py .

# Install the dependencies
RUN pip install flask

# Expose the new port
EXPOSE 5004

# Command to run the app
CMD ["python", "app.py"]

