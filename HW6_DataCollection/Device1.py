from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4 # '파일 크기': 4바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)
print('Device1 server is running...')

while True:
    conn, addr = sock.accept()
    msg = conn.recv(BUF_SIZE) #'Hello' 메시지 수신
    
    if not msg:
        conn.close()
        continue
    elif msg != b'Hello':
        print('client:', addr, msg.decode())
        conn.close()
        continue
    else:
        print('client:', addr, msg.decode())
    
    # 'Request'라고 적으세요~ 메시지 전송
    conn.send(b'Type \'Request\'')
    
    # Request 수신
    req = conn.recv(BUF_SIZE)
    if not req:
        conn.close()
        continue
    elif req.decode() != 'Request':
        conn.close()
        continue
    client_ans = req.decode()
    print('client:', addr, client_ans)

    # 데이터 임의로 생성 , 송신
    temp = random.randint(0,40)
    humi = random.randint(0,100)
    illum = random.randint(70,150)
    print(f'Temp : {temp}, Humi : {humi}, Illum : {illum}')
    conn.send(temp.to_bytes(4,'big'))
    conn.send(humi.to_bytes(4,'big'))
    conn.send(illum.to_bytes(4,'big'))
    print('sended')
    # msg = conn.recv(BUF_SIZE) # 'quit' 메시지 수신
    # if not msg:
    #     pass
    # else:
    #     print('client:', addr, msg.decode())
    # conn.close()