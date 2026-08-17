import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = "."  # folder where landing-page.html is located

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == "/":
            self.path = "/landing-page.html"
        return super().do_GET()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"Serving landing-page.html at {url}")
    webbrowser.open(url)
    httpd.serve_forever()
