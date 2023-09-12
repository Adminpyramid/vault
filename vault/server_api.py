import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import requests


# Define a custom request handler class
class RequestHandler(BaseHTTPRequestHandler):
    def _send_response(self, status, message):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(message).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode())

        # Process the received data
        vault_token = data["vaultToken"]
        os.environ["token"] = vault_token

        # Example usage:
        data_to_send = {
            "message": "ciphertext",
            "vaultToken": vault_token,  # Include the Vault token
        }

        result = send_data_to_django(data_to_send)
        print(result)
        # Send a response back to Node.js (optional)
        response_data = {'message': 'Data received successfully'}
        self._send_response(200, response_data)


def run():
    host = 'localhost'
    port = 8080
    server_address = (host, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Starting Python server on {host}:{port}')

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print('Stopping Python server')


def send_data_to_django(data):
    """
    Sends data to a Django API endpoint.

    Args:
        data (dict): The data to send.

    Returns:
        bool: True if the data was sent successfully, False otherwise.
    """
    try:
        # Define the URL of the Django API endpoint
        url = "http://localhost:8000/receive_data/"

        # Send a POST request to the Django API endpoint with JSON data
        response = requests.post(url, json=data)

        if response.status_code == 200:
            return True
        else:
            print(f"Error sending data to Django. Status Code: {response.status_code}")
            return False
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return False


if __name__ == '__main__':
    run()
