import socket

# 서버의 IP 주소와 포트 번호를 미리 지정해둠
SERVER_IP = 'localhost'
SERVER_PORT = 9000

# 서버와 통신하기 위한 소켓 객체 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # 사용자로부터 문자열 입력 받음
    user_input = input("Enter the message: ")

    # 입력 받은 문자열이 "quit" 이면 프로그램 종료
    if user_input == "quit":
        client_socket.sendto(user_input.encode(), (SERVER_IP, SERVER_PORT))
        break

    # 서버로부터 응답 받을 때까지 반복
    while True:
        # 서버에게 입력 받은 문자열 전송
        client_socket.sendto(user_input.encode(), (SERVER_IP, SERVER_PORT))
        # 서버로부터 응답을 받음
        server_response, server_address = client_socket.recvfrom(1024)
        # 서버로부터 받은 응답을 화면에 출력
        print(server_response.decode())
        # "OK"를 받으면 반복문을 탈출
        break

# 소켓 닫기
client_socket.close()