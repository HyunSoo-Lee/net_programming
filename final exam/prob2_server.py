import socket
import time
import threading

clients = [] # 클라이언트 목록
server_address = ('', 7777)

# TCP 소켓 생성
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(server_address)
s.listen(5)

print('Server Started')

device_data = dict()
device_data = {'1' : [], '2' : []}

def insert(num1, num2):
    global device_data
    device_data[num1].append(num2)

def thread_task(lock, num1, num2):
    lock.acquire()
    insert(num1, num2)
    lock.release()

# 클라이언트 처리 스레드
def client_thread(lock, conn, addr):
    # 새로운 클라이언트이면 목록에 추가
    if (conn, addr) not in clients:
        print('new client', addr)
        clients.append((conn, addr))
        #print(clients)

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
        response = data.decode()
        nums = response.split()
        thread_task(lock, nums[0], nums[1])
        print(device_data)
        # 모든 클라이언트에게 전송
    conn.close()

while True:
    lock = threading.Lock()
    # 연결 요청 대기
    conn, addr = s.accept()
    # 새로운 클라이언트 연결 처리 스레드 생성
    threading.Thread(target=client_thread, args=(lock, conn, addr)).start()
