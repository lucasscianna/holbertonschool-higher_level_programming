#!/usr/bin/python3
"""
Module that implements a simple HTTP API server
using Python's http.server module.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Custom request handler for the simple API.

    Handles GET requests and routes them to
    different endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests and route to the
        appropriate endpoint.
        """
        if self.path == "/":
            self._send_text_response(
                200,
                "Hello, this is a simple API!"
            )

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._send_json_response(200, data)

        elif self.path == "/status":
            self._send_text_response(200, "OK")

        else:
            self._send_text_response(404, "Endpoint not found")

    def _send_text_response(self, status_code, message):
        """
        Send a plain text HTTP response.

        Args:
            status_code (int): HTTP status code.
            message (str): Message to send.
        """
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, status_code, data):
        """
        Send a JSON HTTP response.

        Args:
            status_code (int): HTTP status code.
            data (dict): Data to convert to JSON.
        """
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        json_data = json.dumps(data)
        self.wfile.write(json_data.encode("utf-8"))


def run(server_class=HTTPServer,
        handler_class=SimpleAPIHandler,
        port=8000):
    """
    Start the HTTP server.

    Args:
        server_class: HTTP server class.
        handler_class: Request handler class.
        port (int): Port number.
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)

    print(f"Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
