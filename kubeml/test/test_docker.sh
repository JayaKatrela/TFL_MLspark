#!/bin/bash

IMAGE_NAME="jayakatrela/tflforecaste:latest"

echo "📦 Building Docker image..."
docker build -t $IMAGE_NAME kubeml/

echo "🚢 Running Docker tests..."
docker run --rm $IMAGE_NAME python3 -m unittest discover -s /app/test -p "test_forecasteml.py"

if [ $? -eq 0 ]; then
    echo "✅ Docker tests passed!"
    exit 0
else
    echo "❌ Docker tests failed."
    exit 1
fi
