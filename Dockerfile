# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy flask-web-app script into the container at /app
COPY flask-web-app.py /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run flask-web-app.py when the container launches
CMD ["python", "flask-web-app.py"]