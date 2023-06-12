from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4 # '파일 크기': 4바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 9999))
sock.listen(10)
print('Device1 server is running...')

# [select]소켓 리스트에 서버 소켓을 추가
#socket_list = [sock]

while True:
    # [select] if 통해 새로운 연결 처리
    conn, addr = sock.accept()
    # if s == sock:
    #         conn, addr = sock.accept()
    #         socket_list.append(conn)
    #         print('New client connected:', addr)

    # else
    # [select] else 통해서 데이터 수신 및 처리
    num = conn.recv(BUF_SIZE) # 넘버 메시지 수신

    if not num:
        conn.close()
        continue
    else:
        num = int.from_bytes(num, 'big')
        print('client:', addr, num)

    temp = 0
    humi = 0
    illum = 0
    result = ''

    if num == 1:
        temp = random.randint(0,40)
        result = f'Temp={temp}'
        conn.send(result.encode())
    elif num == 2:
        humi = random.randint(0,100)
        result = f'Humi={humi}'
        conn.send(result.encode())

    print('sended : ', result)