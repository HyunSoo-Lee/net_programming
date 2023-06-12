from socket import *
import os
import threading

def open_file(filename, mimeType, client, f):
    if os.path.isfile(filename):
        # HTTP header
        client.send(b'HTTP/1.1 200 OK\r\n')
        client.send(('Content-Type: ' + mimeType + '\r\n').encode())
        client.send(b'\r\n')

        # HTTP body
        # 만약 이미지 읽는 코드 있으면 무조건 이거 사용하자
        while True:
            data = f.read(1024)
            if not data:
                break
            client.send(data)

    # 소켓 닫기
    client.close()

def thread_handler(client):
    f = open('iot.png', 'rb')
    mimeType = 'image/png'
    open_file('iot.png', mimeType, client, f)

    # 소켓 닫기
    client.close()

# localhost/8080
s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(10)

while True:
    client, addr = s.accept()
    # 새로운 스레드 생성하여 요청 처리
    th = threading.Thread(target=thread_handler, args=(client,))
    th.start()
s.close()
