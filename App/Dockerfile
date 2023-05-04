# Set the base image
FROM python:3.9

# Copy the code into the container
COPY . /app

# Set the working directory
WORKDIR /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8080

# Run the command to start the app
CMD ["python", "1XBetCrashUpdater.py"]
