import socket
from time import *

# 서버의 IP, PORT
HOST = 'localhost'
PORT = 9000

# 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 사용자로부터 문자열 입력 받음
    user_input = input("Enter the message: ")

    # 입력 받은 문자열이 "quit" 이면 프로그램 종료
    if user_input == "quit":
        client_socket.sendto(user_input.encode(), (HOST, PORT))
        break

    # 서버로부터 응답 받을 때까지 반복
    while True:
        j = 0
        timeoutT = 1 # 1초
        # 서버에게 입력 받은 문자열 전송
        client_socket.sendto(user_input.encode(), (HOST, PORT))
        client_socket.settimeout(timeoutT)
        # 서버로부터 응답을 받음
        try:
            server_response, server_address = client_socket.recvfrom(1024)
        except timeout:
            if j == 3:
                print('Fail')
                break
            j += 1
            sleep(2)
        # 서버로부터 받은 응답을 화면에 출력
        print(server_response.decode())
        break

# 소켓 닫기
client_socket.close()