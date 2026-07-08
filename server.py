import http.server
import socketserver
import os

PORT = 3000
DIRECTORY = "c:/Projects/MakeMyPC"

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def log_message(self, format, *args):
        pass  # suppress logs

with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
    print(f"Serving at http://localhost:{PORT} (no-cache mode)")
    httpd.serve_forever()
