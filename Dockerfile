# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Tkinter since it's needed for GUI applications
RUN apt-get update && apt-get install -y python3-tk

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Python script when the container launches
CMD ["python3", "app.py"]
