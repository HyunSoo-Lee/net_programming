import socket
import threading

def handler(sock):
    while True:
        msg = sock.recv(1024)
        if not msg:
            break
        print(msg.decode())
    
# TCP 소켓 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))

my_id = input('ID를 입력하세요: ')
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())
