from flask import Flask, jsonify
import datetime
import socket

# Initialize a Flask application
app = Flask(__name__)

# Define the route for the root URL
@app.route('/')
def home(): # Create a JSON response containing the current UTC timestamp and the hostname
    return jsonify({
        'timestamp': datetime.datetime.utcnow().isoformat(), # Current UTC timestamp in ISO 8601 format
        'hostname': socket.gethostname() # Hostname of the machine running the Flask app
    })

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # The app will be accessible from any IP address on port 5000
