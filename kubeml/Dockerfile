FROM openjdk:8-jre-slim-buster

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install PySpark
RUN pip3 install pyspark==3.2.1
RUN pip3 install findspark
RUN pip3 install numpy
# Set the working directory
WORKDIR /app

# Copy the PySpark application code into the container
COPY forcasteml.py .
COPY test/test_forecasteml.py /app/test/test_forecasteml.py
COPY test/test_docker.sh /app/test/test_docker.sh  # Copy the Docker test script into the container

# Give execute permission to the test script
RUN chmod +x /app/test_docker.sh

# Set the entrypoint
CMD ["spark-submit", "--master", "local[*]", "forcasteml.py"]
#CMD ["./test_docker.sh"]

