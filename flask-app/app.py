# Import necessary modules
from flask import Flask, jsonify  # Flask is the web framework, jsonify is used to return JSON responses
import datetime  # To get the current date and time
import socket  # To get the hostname of the machine running the app
from prometheus_flask_exporter import PrometheusMetrics  # For monitoring and metrics

# Initialize the Flask application
app = Flask(__name__)

# Set up Prometheus metrics monitoring
metrics = PrometheusMetrics(app)

# Define the root route ('/') of the web application
@app.route('/')
def home():
    # When a request is made to the root route, return a JSON response
    # containing the current timestamp and the hostname of the server
    return jsonify({
        'timestamp': datetime.datetime.utcnow().isoformat(),  # Current time in ISO format
        'hostname': socket.gethostname()  # Hostname of the machine
    })

# If this script is run directly, start the Flask web server
if __name__ == '__main__':
    # Run the app on all available IP addresses on port 5000
    app.run(host='0.0.0.0', port=5000)