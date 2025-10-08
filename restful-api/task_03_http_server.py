#!/usr/bin/python3

"""Develop a simple API using Python with the `http.server` module."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleServer(BaseHTTPRequestHandler):
    """A subclass of BaseHTTPRquestHandler."""

    def do_GET(self):
        """A new do_GET method."""

        print(f"Requête reçue pour : {self.path}")

        if self.path == "/" or self.path == "":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK.")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({"version": "1.0", "description":
                            "A simple API built with http.server"}).encode())

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server = HTTPServer(('', PORT), SimpleServer)
    print(f'Server running on port {PORT}')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        server.server_close()
