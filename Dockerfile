# base image
FROM python:3.9-slim

# working directory in  container
WORKDIR /app

# install required packages
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install app dependencies
RUN pip install Flask==2.0.1
RUN pip install Flask-MySQLdb==0.2.0
RUN pip install requests==2.26.0
RUN pip install Werkzeug==2.2.2

# Copy the rest of the application code

#entry point to run application
CMD ["python", "app.py"]
