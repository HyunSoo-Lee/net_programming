from http.server import HTTPServer, BaseHTTPRequestHandler

HOST_IP = 'localhost'
PORT = 8080

#서버 작성 방법-> BaseHTTPRequestHandler를 상속받는 클래스 작성 -> do_Get, do_Post 등의 함수 사용하여 서버 열면 된당.

class http_handler(BaseHTTPRequestHandler):
    # def do_GET(self):
    #     self.send_response(200) # 상태코드 설정
    #     self.end_headers() # 헤더 정보 추가
    #     self.wfile.write(b'<h1>Hello, IoT!<h1>') # body 작성
    def do_GET(self):
        self.route()
    def route(self):
        #route 메소드 : 경로에 따라 적절하게 처리해주는 함수
        if self.path == '/':
            self.send_html()
        elif self.path == '/iot.png':
            self.send_image()
        else:
            self.response(404, 'Not Found')
    def send_html(self):
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers()
        #html 파일 핸들링
        with open('index.html', 'r', encoding='utf-8') as f:
            msg = f.read()
            self.wfile.write(msg.encode('euc-kr'))
    def send_image(self):
        self.send_response(200)
        self.send_header('Contents-type', 'image/png')
        self.end_headers()
        with open('iot.png', 'rb') as f:
            msg = f.read()
            self.wfile.write(msg)
    def response(self, status_code, body): 
        self.send_response(status_code) 
        self.send_header('Content-type', 'text/plain') 
        self.end_headers() 
        self.wfile.write(body.encode())

httpd = HTTPServer((HOST_IP, PORT), http_handler)
print('Serving HTTP on {}:{}'.format(HOST_IP, PORT))
httpd.serve_forever()