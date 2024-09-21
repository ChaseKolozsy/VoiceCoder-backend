from flask import Flask, request, jsonify
import requests
import paramiko
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def create_app():
    app = Flask(__name__)
    
    # SSH connection details
    SSH_HOST = os.getenv('SSH_HOST')
    SSH_USER = os.getenv('SSH_USER')
    SSH_PASSWORD = os.getenv('SSH_PASSWORD')
    HOME_SERVER_PORT = os.getenv('HOME_SERVER_PORT')

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def start_home_server():
        try:
            ssh_client.connect(SSH_HOST, username=SSH_USER, password=SSH_PASSWORD)
            stdin, stdout, stderr = ssh_client.exec_command('python3 /path/to/home_server.py')
            # You might want to check stderr for any errors
            return True
        except Exception as e:
            print(f"Error starting home server: {e}")
            return False

    @app.route('/api/start_server', methods=['POST'])
    def start_server():
        if start_home_server():
            return jsonify({"message": "Home server started successfully"}), 200
        else:
            return jsonify({"error": "Failed to start home server"}), 500

    @app.route('/api/<path:subpath>', methods=['GET', 'POST'])
    def proxy(subpath):
        home_server_url = f"http://localhost:{HOME_SERVER_PORT}"
        if request.method == 'GET':
            resp = requests.get(f"{home_server_url}/{subpath}", params=request.args)
        elif request.method == 'POST':
            resp = requests.post(f"{home_server_url}/{subpath}", json=request.json)
        
        return jsonify(resp.json()), resp.status_code

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)