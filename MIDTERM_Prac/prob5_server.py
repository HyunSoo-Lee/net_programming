#20201514 이현수
from socket import *
import random

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(10)
print('IoT Device is running...')
conn, addr = sock.accept()

while True:
    temp = 0
    humi = 0
    illm = 0
    num = conn.recv(1024)
    num = num.decode() 
    if not num:
        continue
    elif num == '1':
        temp = random.randint(1,50)
        conn.send(temp.to_bytes(4, 'big'))
        conn.send(humi.to_bytes(4, 'big'))
        conn.send(illm.to_bytes(4, 'big'))
        continue
    elif num == '2':
        humi = random.randint(1,100)
        conn.send(temp.to_bytes(4, 'big'))
        conn.send(humi.to_bytes(4, 'big'))
        conn.send(illm.to_bytes(4, 'big'))
        continue
    elif num == '3':
        illm = random.randint(1,150)
        conn.send(temp.to_bytes(4, 'big'))
        conn.send(humi.to_bytes(4, 'big'))
        conn.send(illm.to_bytes(4, 'big'))
        continue
    else:
        conn.close()
    
    