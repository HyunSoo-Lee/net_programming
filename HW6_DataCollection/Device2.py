from socket import *
import random

BUF_SIZE = 1024
LENGTH = 4 # '파일 크기': 4바이트

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(10)
print('Device2 server is running...')

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
    heartrate = random.randint(40,140)
    step = random.randint(2000,6000)
    cal = random.randint(1000,4000)
    print(f'Heart rate : {heartrate}, Step : {step}, Calorie : {cal}')
    conn.send(heartrate.to_bytes(4,'big'))
    conn.send(step.to_bytes(4,'big'))
    conn.send(cal.to_bytes(4,'big'))
    print('sended')
    # msg = conn.recv(BUF_SIZE) # 'quit' 메시지 수신
    # if not msg:
    #     pass
    # else:
    #     print('client:', addr, msg.decode())
    #     conn.close()