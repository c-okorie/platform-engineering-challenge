#!/bin/bash

# Check if Minikube is installed
if ! command -v minikube &> /dev/null
then
    echo "Minikube not found. Installing Minikube..."
    curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    chmod +x minikube
    sudo mv minikube /usr/local/bin/
else
    echo "Minikube is already installed."
fi

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null
then
    echo "kubectl not found. Installing kubectl..."
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    chmod +x kubectl
    sudo mv kubectl /usr/local/bin/
else
    echo "kubectl is already installed."
fi

# Start Minikube cluster
echo "Starting Minikube..."
minikube start

# Check if Minikube started successfully
if [ $? -ne 0 ]; then
    echo "Failed to start Minikube. Exiting..."
    exit 1
fi

# Verify Minikube status
minikube status

# Set up kubectl context
echo "Setting up kubectl context..."
kubectl config use-context minikube

# Verify kubectl context
kubectl cluster-info

echo "Minikube cluster is up and running!"

# Enable Minikube addons
 echo "Enabling Minikube addons..."
 minikube addons enable dashboard
 minikube addons enable ingress

# Verify the nodes in the cluster
kubectl get nodes

echo "Minikube bootstrap complete. You can now use kubectl to interact with your local Kubernetes cluster."
