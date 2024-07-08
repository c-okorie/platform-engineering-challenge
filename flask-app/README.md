# Flask App

## Description

This is a simple Flask application that returns the current timestamp and hostname.

## How to Build the Application

1. Clone the repository
   
   git clone https://github.com/c-okorie/platform-engineering-challenge.git 
   git checkout platform    # switches to the platform branch that has the configuration files
   cd flask-app

2. Test the application locally 

    pip install Flask # Install Flask
    python app.py # Run the Flask application 

    You should see output like the image below indicating that the Flask app is running:


    Open a web browser and go to http://127.0.0.1:5000/. You should see a JSON response similar to the image below:
    Press CTRL+C to quit

3. Build the Docker image

docker build -t emmyforlife/flask-app:latest . # emmyforlife is my dockerhub username and flask-app is the name of the repository in dockerhub where the image will be pushed

4. Push the Docker image to Docker Hub

docker push emmyforlife/flask-app:latest # Note: you have to login to your dockerhub account, simply run docker login in your terminal and provide the username and password

##  Setup the Testing Environment
## For this demo, I used a local instance of minikube

1. Install Minikube

2. Start Minikube

3. Deploy the application as described above.

Instructions on how to install minikube for different operating systems can be found in this link https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Fx86-64%2Fstable%2Fbinary+download

## How to Deploy the Application

1. Apply the Kubernetes manifests

kubectl apply -f kubernetes/

2. Check the status of the deployment

kubectl get deployments
kubectl get services
kubectl get ingress