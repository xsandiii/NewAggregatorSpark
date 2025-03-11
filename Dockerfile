# Use a Python base image
FROM python:3.9

# Set environment variables for Java (required for Spark)
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Install system dependencies
RUN apt-get update && apt-get install -y openjdk-17-jdk-headless

# Set the working directory inside the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install Python dependencies, including PySpark
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask API port
EXPOSE 8777

# Run the Flask app
CMD ["python", "app.py"]
