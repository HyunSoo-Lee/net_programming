from http.server import HTTPServer, BaseHTTPRequestHandler
class http_handler(BaseHTTPRequestHandler): 
    def do_GET(self):
        self.send_response(200) 
        self.end_headers()
        with open('iot.png', 'rb') as f:
            msg = f.read()
            self.wfile.write(msg)

httpd = HTTPServer(('localhost', 8080), http_handler) 
print('Serving HTTP on {}:{}'.format('localhost', 8080)) 
httpd.serve_forever()
            