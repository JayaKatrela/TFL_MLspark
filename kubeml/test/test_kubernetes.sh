#!/bin/bash

JOB_NAME="tfl_kubeml"

echo "📊 Waiting for Kubernetes job to complete..."
kubectl wait --for=condition=complete job/$JOB_NAME --timeout=300s

echo "📜 Fetching Kubernetes logs..."
kubectl logs job/$JOB_NAME

MODEL_DIR="/var/lib/jenkins/workspace/TfL_KubeMl/kubeml_pr/models"
if [ -d "$MODEL_DIR" ]; then
    echo "✅ Model output exists!"
    exit 0
else
    echo "❌ Model output missing!"
    exit 1
fi
