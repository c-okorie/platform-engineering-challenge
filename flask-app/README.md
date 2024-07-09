 # Get Started with Your Powerful Flask App

Unleash the power of Kubernetes for your Flask application! The application is a service that responds to an HTTP GET request and returns timestamp and hostname.
This comprehensive solution outlines the steps for containerization and deployment with best practices. Leverage Prometheus for robust monitoring and optimize your Docker image size for efficient workflows. Enjoy a seamless setup experience with detailed instructions and local Kubernetes testing capabilities.

## Key Features:

* **Intuitive File Structure:** The project boasts a well-organized structure, making navigation and maintenance a breeze.
* **Local Development:** Easily run the application locally for testing and refinement.
* **Dockerized Deployment:** Package your application in a self-contained Docker image for simplified deployment across environments.
* **Kubernetes Integration:** Seamlessly integrate your application within a Kubernetes cluster for scalable and resilient operations.

## Prerequisites:

* Git version control system (https://git-scm.com/).
* Python 3 (https://www.python.org/downloads/)
* Docker (https://www.docker.com/) (optional for containerized deployment)
* Kubernetes cluster (optional for advanced deployment)

## Installation:

### 1. Clone the repository
   ```
   git clone https://github.com/c-okorie/platform-engineering-challenge.git 
   cd flask-app
  ```
### 2. Test the application locally 
* Install Flask:
    ```
    pip install Flask
    ```
* Run the Application:
    ```
    python app.py 
    ```
* Open http://127.0.0.1:5000/ in your web browser to view a JSON response, indicating successful application startup.
    Press CTRL+C on your terminal to quit

### 3. Build Docker Image

* Build the Docker image:
     ```
    docker build -t emmyforlife/flask-app:latest . 
    ```
     _Replace emmyforlife with your Docker Hub username._
  
* Push the image to Docker Hub or other image repository (requires login):
     ```
    docker login
    docker push emmyforlife/flask-app:latest
     ```

### 4.  Setup Testing Environment (For this demo, I used a local instance of minikube)
I have added the `bootstrap_minikube.sh` file to bootstrap the the minikube cluster for local testing.

Further details can be found in the official Minikube website in the following link:
https://minikube.sigs.k8s.io/docs/start/


### 5 Deployment

* Apply Kubernetes manifests:
    ```
    kubectl apply -f kubernetes/
    ```
* Monitor deployment status:
    ```
    kubectl get deployments
    kubectl get services
    kubectl get ingress
    ```
### 6 Monitoring/Metrics

* Add Helm Repositories:
    ```
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo add grafana https://grafana.github.io/helm-charts
    helm repo update
    ```
* Install Prometheus and Grafana:
    ```
    helm install prometheus prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
    helm install grafana grafana/grafana --namespace monitoring
    ```
* Accessing the Service:
    ```
    kubectl port-forward -n monitoring svc/prometheus-kube-prometheus-prometheus 9090:9090
    kubectl port-forward -n monitoring svc/grafana 3000:3000
    ```
    You can access Prometheus at `http://localhost:9090` and `Grafana at http://localhost:3000`
* Final steps, add Prometheus as data source in Grafana and import dashboards
