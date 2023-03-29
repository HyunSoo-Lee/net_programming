from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Write the operation you want to perform : ')
    if msg == 'q':
        break
    s.send(msg.encode())
    #int.from_bytes(StuId, 'big')
    #print('Received message:', s.recv(1024).decode())
    rsp = s.recv(1024)
    print('Received message:', rsp.decode())
s.close()