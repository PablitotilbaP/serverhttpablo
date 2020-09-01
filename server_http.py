#!/usr/bin/env python3
import os
import json
import socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


port = int(os.getenv("PORT"))


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('94.75.67.141', 8080))
        client.send(b"I am client .........hello")
        client.close()

    # def do_POST(self):
    #     content_length = int(self.headers['Content-Length'])
    #     body = self.rfile.read(content_length)
    #     body_dic = json.loads(body.decode())["dic"]
    #     list = body_dic.split(":")
    #
    #     public_ip = list[0]
    #     public_port = int(list[1])
    #     print(public_ip)
    #     print(public_port)
    #
    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     client.connect((public_ip, public_port))
    #     client.send(b"I am server .........hello")
    #     client.close()
    #
    #
    #     self.send_response(200)
    #     self.end_headers()
    #     response = BytesIO()
    #     response.write(b'This is POST request. ')
    #     response.write(b'Received: ')
    #     response.write(body)
    #     self.wfile.write(response.getvalue())


# print('Server listening on port: ',port)
httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
httpd.serve_forever()


# print('Server listening on port 8000...')
# httpd = socketserver.TCPServer(('', 8000), Handler)
# httpd.serve_forever()
