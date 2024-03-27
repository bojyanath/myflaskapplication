# base image
FROM python:3.9-slim
# working directory in  container
WORKDIR /app
# Copy the rest of the application code
COPY . .
#entry point to run application
CMD ["python", "app.py"]
