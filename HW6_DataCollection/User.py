from socket import *
import sys
import time

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트
f = open('data.txt','w')

s = socket(AF_INET, SOCK_STREAM)
while True : 
    port = input('Enter the device number (or quit) : ')
    if port == '1':
        s.connect(('localhost', 7777))
    elif port == '2':
        s.connect(('localhost', 9000))
    elif port == 'quit':
        f.close()
        s.connect(('localhost', 7777))
        s.send(b'quit') # 'Bye' 메시지 전송
        s.close()
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 9000))
        s.send(b'quit') # 'Bye' 메시지 전송
        s.close()
        break
    else:
        print('You write wrong device number')
        s.close()
    s.send(b'Hello')  # 'Hello' 메시지 전송

    msg = s.recv(BUF_SIZE)  # 'Request'라고 적으세요~ 메시지 수신
    if not msg:
        s.close()
        sys.exit()
    elif msg != b'Type \'Request\'':
        print('server:', msg.decode())
        s.close()
        sys.exit()
    else:
        print('Server:', msg.decode())

    # Request 메세지 전송
    req = input('Enter : ')
    s.send(req.encode())  
    
    now = time.localtime()
    nowtime = time.strftime("%a %b %d %H:%M:%S %Y", now)
    
    if port == '1':
        temp = s.recv(1024)
        temp = int.from_bytes(temp, 'big')
        humi = s.recv(1024)
        humi = int.from_bytes(humi, 'big')
        illum = s.recv(1024)
        illum = int.from_bytes(illum, 'big')
        print(f'{nowtime}: Temp={temp}, Humid={humi}, Iilum={illum}')
        f.write(f'{nowtime}: Temp={temp}, Humid={humi}, Iilum={illum}\n')
    elif port == '2':
        heartrate = s.recv(1024)
        heartrate = int.from_bytes(heartrate, 'big')
        step = s.recv(1024)
        step = int.from_bytes(step, 'big')
        cal = s.recv(1024)
        cal = int.from_bytes(cal, 'big')
        print(f'{nowtime}: Heartbeat={heartrate}, Steps={step}, Cal={cal}')
        f.write(f'{nowtime}: Heartbeat={heartrate}, Steps={step}, Cal={cal}\n')
    s.close()
    s = socket(AF_INET, SOCK_STREAM)