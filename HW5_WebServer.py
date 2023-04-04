from socket import *
import os

def parsing(req):
    #req = "GET /index.html HTTP/1.1"
    filename = req[0].split(' ')[1]
    filename = filename[1:]
    return filename

def open_file(filename, mimeType, c, f):
    if os.path.isfile(filename):
        # 파일이 있을때
        # HTTP header 
        c.send(b'HTTP/1.1 200 OK\r\n')
        contype_str = 'Content-Type: ' + mimeType + '\r\n'
        c.send(contype_str.encode())
        c.send(b'\r\n')

        # HTTP body 
        data = f.read()
        if filename == 'index.html':
            c.send(data.encode('euc-kr'))
        else:
            c.send(data)
    else:
        # 파일이 없을때
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    
#http://127.0.0.1/index.html
s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
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
    open_file(filename, mimeType, c, f)

    #소켓 닫기
    c.close()
