#!/usr/bin/env python3

"""Develop a simple API using Python with the `http.server` module."""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class Serveur(BaseHTTPRequestHandler):
    """A subclass of BaseHTTPRquestHandler."""

    def do_GET(self):
        """A new do_GET method."""
        if self.path == "/" or self.path == "":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"This is an API.")

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

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
