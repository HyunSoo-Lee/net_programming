import socket
import select

clients = []  # 클라이언트 목록
server_address = ('', 2500)

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(server_address)
s.listen(5)

print('Server Started')

# 클라이언트 처리 함수
def client_handler(client_socket):
    data = client_socket.recv(1024)
    if not data:
        return False
    # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
    if b'quit' in data:
        clients.remove(client_socket)
        return False
    for client in clients:
        if client != client_socket:
            client.send(data)
    return True

while True:
    # 읽기 가능한 소켓 리스트
    r_sock, w_sock, e_sock = select.select([s] + clients, [], [])

    for sock in r_sock:
        if sock is s:
            # 새로운 클라이언트 연결 처리
            conn, addr = s.accept()
            clients.append(conn)
            print('New client', addr)
        else:
            # 클라이언트 소켓으로 데이터 수신 및 처리
            if not client_handler(sock):
                sock.close()
                clients.remove(sock)
