from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


class HttpGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health/':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write('{"status": "OK"}'.encode())
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write('Not found'.encode())


server = HTTPServer(('0.0.0.0', 8000), HttpGetHandler)

if __name__ == '__main__':
  try:
      server.serve_forever()
  except KeyboardInterrupt:
      server.server_close()