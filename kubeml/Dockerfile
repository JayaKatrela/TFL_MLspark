FROM openjdk:8-jre-slim-buster

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark and other dependencies
RUN pip3 install pyspark==3.2.1
RUN pip3 install findspark
RUN pip3 install numpy

# Set the working directory inside the container
WORKDIR /app

# Copy PySpark application code into the container
COPY forcasteml.py .  # Copy the main application code

# Copy the unit tests and Docker test script into the container
COPY test/test_forecasteml.py /app/test/test_forecasteml.py  # Copy the PySpark unit tests
COPY test/test_docker.sh /app/test/test_docker.sh  # Copy the Docker test script

# Make the Docker test script executable
RUN chmod +x /app/test/test_docker.sh
RUN chmod +x kubeml/test/test_docker.sh


# Set the entrypoint for the container
CMD ["spark-submit", "--master", "local[*]", "forcasteml.py"]
