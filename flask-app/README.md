# Flask App

## Description

This is a simple Flask application that returns the current timestamp and hostname.

## How to Build the Application

1. Clone the repository
   
   git clone https://github.com/c-okorie/platform-engineering-challenge.git
   git checkout platform    # switches to the platform branch that has the configuration files
   cd flask-app

2. Test the application locally 

3. Build the Docker image

docker build -t your-dockerhub-username/flask-app:latest .

4. Push the Docker image to Docker Hub

docker push your-dockerhub-username/flask-app:latest

## How to Deploy the Application

1. Apply the Kubernetes manifests

kubectl apply -f kubernetes/

2. Check the status of the deployment

kubectl get deployments
kubectl get services
kubectl get ingress

##  Setup the Testing Environment
## For this demo, I used a local instance of minikube

1. Install Minikube

2. Start Minikube

3. Deploy the application as described above.

Instructions on how to install minikube for different operating systems can be found in this link https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Fx86-64%2Fstable%2Fbinary+download
