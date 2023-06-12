from socket import *
import select
import random

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 9999))
sock.listen(10)
print('Device1 server is running...')

# [select]소켓 리스트에 서버 소켓을 추가
socket_list = [sock]

while True:
    # [select]
    # select 함수를 사용하여 소켓 모니터링
    r_sock, w_sock, e_sock = select.select(socket_list, [], [])

    for s in r_sock:
        # 새로운 연결 요청 처리
        if s == sock:
            conn, addr = sock.accept()
            socket_list.append(conn)
            print('New client connected:', addr)
        # [select] till here
        
        # 데이터 수신 및 처리
        else:
            num = s.recv(BUF_SIZE)  # 'Hello' 메시지 수신

            if not num:
                s.close()
                socket_list.remove(s)
                continue
            else:
                num = int.from_bytes(num, 'big')
                print('Client:', s.getpeername(), num)

            temp = 0
            humi = 0
            illum = 0
            result = ''

            if num == 1:
                temp = random.randint(0, 40)
                result = f'Temp={temp}'
                s.send(result.encode())
            elif num == 2:
                humi = random.randint(0, 100)
                result = f'Humi={humi}'
                s.send(result.encode())

            print('Sent:', result)
