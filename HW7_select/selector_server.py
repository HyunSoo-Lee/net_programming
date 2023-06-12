import socket
import selectors
import time

clients = []  # 클라이언트 목록
server_address = ('', 2500)

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(server_address)
s.listen(5)

print('Server Started')

# 선택자 생성
selector = selectors.DefaultSelector()

# 클라이언트 처리 함수
def client_handler(conn, addr):
    # 새로운 클라이언트이면 목록에 추가
    if (conn, addr) not in clients:
        print('new client', addr)
        clients.append((conn, addr))

    while True:
        data = conn.recv(1024)
        if not data:
            break
        # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if 'quit' in data.decode():
            if (conn, addr) in clients:
                print(addr, 'exited')
                clients.remove((conn, addr))
                continue
        print(time.asctime() + str(addr) + ':' + data.decode())
        # 모든 클라이언트에게 전송
        for client in clients:
            if client[1] != addr:
                client[0].send(data)

    conn.close()
    # 선택자에서 이벤트 등록 해제
    selector.unregister(conn)
    conn.close()

def accept_handler(sock):
    conn, addr = sock.accept()
    print('New client', addr)
    # 연결된 클라이언트 소켓을 선택자에 등록
    selector.register(conn, selectors.EVENT_READ, client_handler)

# 서버 소켓을 선택자에 등록
selector.register(s, selectors.EVENT_READ, accept_handler)

while True:
    # 선택자에 등록된 소켓 이벤트를 감지
    events = selector.select()

    for key, _ in events:
        callback = key.data
        callback(key.fileobj)
