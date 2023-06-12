import selectors
from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 9999))
sock.listen(10)
print('Device1 server is running...')

sel = selectors.DefaultSelector()

# 기존 함수를 연결/송수신을 나누어

# 새로운 클라이언트로부터 연결을 처리하는 함수 [연결], s대신 
def accept(sock, mask):
    conn, addr = sock.accept()
    print('Connected from', addr)

    # 새로운 클라이언트 소켓을 선택기에 등록
    sel.register(conn, selectors.EVENT_READ, read)

# 기존 클라이언트로부터 수신한 데이터를 처리하는 함수 [송수신]
def read(conn, mask):
    num = conn.recv(BUF_SIZE)  # 'Hello' 메시지 수신

    if not num:
        sel.unregister(conn)
        conn.close()
        return
    else:
        num = int.from_bytes(num, 'big')
        print('Client:', conn.getpeername(), num)

    temp = 0
    humi = 0
    result = ''

    if num == 1:
        temp = random.randint(0, 40)
        result = f'Temp={temp}'
        conn.send(result.encode())
    elif num == 2:
        humi = random.randint(0, 100)
        result = f'Humi={humi}'
        conn.send(result.encode())

    print('Sent:', result)

# 서버 소켓을 선택기에 등록 [여기부턴 그냥 그대로 쓰자]
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()

    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
