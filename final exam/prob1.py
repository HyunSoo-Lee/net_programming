from socket import *
import os
import selectors

def parsing(req):
    # req = "GET /index.html HTTP/1.1"
    filename = req[0].split(' ')[1][1:]
    return filename

def open_file(filename, mimeType, c, f):
    if os.path.isfile(filename):
        # HTTP header 
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(('Content-Type: ' + mimeType + '\r\n').encode())
        c.send(b'\r\n')

        # HTTP body 
        data = f.read()
        if filename == 'index.html':
            c.send(data.encode('euc-kr'))
        else:
            c.send(data)
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    
s = socket()
s.bind(('localhost', 8080))
s.listen(10)

sel = selectors.DefaultSelector()

# 새로운 클라이언트로부터 연결을 처리하는 함수 [연결], s대신 
def accept(sock, mask):
    conn, addr = sock.accept()
    print('Connected from', addr)
    # 새로운 클라이언트 소켓을 선택기에 등록
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')
    # 파일 이름 파싱
    filename = parsing(req)
    
    # 웹 서버 코드 작성

    # 파일 분류
    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'
    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'

    # 각 객체(파일 또는 문자열) 전송
    open_file(filename, mimeType, conn, f)

# 서버 소켓을 선택기에 등록 [여기부턴 그냥 그대로 쓰자]
sel.register(s, selectors.EVENT_READ, accept)

while True:
    events = sel.select()

    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)