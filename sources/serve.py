import http.server
import socketserver

PORT = 3000
DIR = "sources/dist"

# list all files
import os
files = os.listdir(DIR)
print("Files in directory: " + str(files))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server started at localhost:" + str(PORT))
    httpd.serve_forever()