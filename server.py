import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = " "
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, directory=DIRECTORY, **kwargs)

with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    httpd.serve_forever()
